import argparse
import concurrent.futures
import os

from tqdm import tqdm


def process_file_pair(args):
    file_id, file_A, file_B = args
    if not os.path.exists(file_B):
        return (file_id, None, file_B)

    with open(file_A, "r") as f:
        txt_pdfalto_A = f.read()
    with open(file_B, "r") as f:
        txt_pdfalto_B = f.read()

    txt_pdfalto_A_spaces = ' '.join(txt_pdfalto_A.split())
    txt_pdfalto_B_spaces = ' '.join(txt_pdfalto_B.split())
    txt_pdfalto_A_spaces_len = len(txt_pdfalto_A_spaces)
    txt_pdfalto_B_spaces_len = len(txt_pdfalto_B_spaces)
    diff_chars_spaces = txt_pdfalto_A_spaces_len - txt_pdfalto_B_spaces_len

    txt_pdfalto_A_no_spaces = ''.join(txt_pdfalto_A.split())
    txt_pdfalto_B_no_spaces = ''.join(txt_pdfalto_B.split())
    txt_pdfalto_A_len = len(txt_pdfalto_A_no_spaces)
    txt_pdfalto_B_len = len(txt_pdfalto_B_no_spaces)
    diff_chars_no_spaces = txt_pdfalto_A_len - txt_pdfalto_B_len

    txt_pdfalto_A_token_len = len(txt_pdfalto_A_spaces.split())
    txt_pdfalto_B_token_len = len(txt_pdfalto_B_spaces.split())
    diff_tokens = txt_pdfalto_A_token_len - txt_pdfalto_B_token_len

    # Use sacrebleu for faster BLEU
    # bleu_score = sacrebleu.sentence_bleu(txt_pdfalto_A_spaces, [txt_pdfalto_B_spaces]).score / 100.0
    # scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
    # rouge_scores = scorer.score(txt_pdfalto_B_spaces, txt_pdfalto_A_spaces)
    # rouge_l_f1 = rouge_scores['rougeL'].fmeasure
    return (file_id, {
        'pdfalto_A': len(txt_pdfalto_A),
        'pdfalto_A_tokens': txt_pdfalto_A_token_len,
        'pdfalto_B': len(txt_pdfalto_B),
        'pdfalto_B_tokens': txt_pdfalto_B_token_len,
        'stats': {
            'diff_chars_no_spaces': diff_chars_no_spaces,
            'diff_chars_spaces': diff_chars_spaces,
            'diff_tokens': diff_tokens,
            # 'bleu': bleu_score,
            # 'rougeL_f1': rouge_l_f1
        }
    }, None)


def compute_run_statistics(input_pdfalto_A, input_pdfalto_B):
    """
    This method computes the statistics between two different runs,
    searching for the common sub-directories and comparing each of them as separated
    corpora
    """
    common_subdirs = extract_common_repositories(input_pdfalto_A, input_pdfalto_B)
    print("Found the following corpus directories: ", common_subdirs)

    documents = {}
    for corpus in common_subdirs:
        print(corpus)
        file_pairs = []
        for root, dirs, files in tqdm(os.walk(os.path.join(input_pdfalto_A, corpus)), desc="Reading files..."):
            for file in files:
                if not file.endswith(".txt"):
                    continue
                # Use only string types for all path operations
                file_path_A = os.path.join(root, file)
                rel_dir = os.path.relpath(root, os.path.join(input_pdfalto_A, corpus))
                if rel_dir == ".":
                    file_id = file.replace(".txt", "")
                else:
                    file_id = os.path.join(rel_dir, file).replace(".txt", "")
                file_A = file_path_A
                file_B = os.path.join(input_pdfalto_B, corpus, rel_dir, file)
                file_pairs.append((file_id, file_A, file_B))

        skipped = []
        processed = {}
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = list(tqdm(executor.map(process_file_pair, file_pairs), total=len(file_pairs), desc="Computing differences..."))

        for file_id, result, skip_path in results:
            if result is None:
                skipped.append((file_id, skip_path))
            else:
                processed[file_id] = result
        documents[corpus] = {
            'processed': processed,
            'skipped': skipped,
            'pdfalto_A': input_pdfalto_A,
            'pdfalto_B': input_pdfalto_B,
            'average': {
                'pdfalto_A': 0,
                'pdfalto_B': 0,
                'diff': 0,
                'perc': 0
            }
        }
        print(f"Processed documents {len(processed)}")
        print(f"Skipped documents {len(skipped)}")
    return documents


def extract_common_repositories(input_pdfalto, input_grobid):
    # Find the subdirectories in the input corpora
    subdirs_pdfalto = [x for x in os.listdir(input_pdfalto)]
    print(f"Found the following corpus directories for PDFAlto A: {subdirs_pdfalto}")
    subdirs_grobid = [x for x in os.listdir(input_grobid)]
    print(f"Found the following corpus directories for PDFAlto B: {subdirs_grobid}")
    # find the common subdirectories
    common_subdirs = [x for x in subdirs_grobid if x in subdirs_pdfalto]
    return common_subdirs


def compute_averages(documents_):
    for process_type, process in documents_.items():
        for corpus, documents in process.items():
            total_pdfalto_A = sum([d['pdfalto_A'] for d in documents['processed'].values()])
            total_pdfalto_B = sum([d['pdfalto_B'] for d in documents['processed'].values()])
            total_diff_chars_no_spaces = sum(
                [d['stats']['diff_chars_no_spaces'] for d in documents['processed'].values()])
            total_diff_chars_spaces = sum([d['stats']['diff_chars_spaces'] for d in documents['processed'].values()])
            matching_documents_chars_no_spaces = sum(
                [d['stats']['diff_chars_no_spaces'] == 0 for d in documents['processed'].values()])
            matching_documents_chars_spaces = sum(
                [d['stats']['diff_chars_spaces'] == 0 for d in documents['processed'].values()])
            total_diff_tokens = sum([d['stats']['diff_tokens'] for d in documents['processed'].values()])
            matching_documents_tokens = sum([d['stats']['diff_tokens'] == 0 for d in documents['processed'].values()])

            documents['average']['pdfalto_A'] = total_pdfalto_A / len(documents['processed'])
            documents['average']['pdfalto_B'] = total_pdfalto_B / len(documents['processed'])
            documents['average']['diff_chars_no_spaces'] = total_diff_chars_no_spaces / len(documents['processed'])
            documents['average']['diff_chars_spaces'] = total_diff_chars_spaces / len(documents['processed'])
            documents['average']['diff_tokens'] = total_diff_tokens / len(documents['processed'])
            documents['average']['matching_documents_chars_spaces'] = matching_documents_chars_spaces
            documents['average']['matching_documents_chars_no_spaces'] = matching_documents_chars_no_spaces
            documents['average']['matching_documents_tokens'] = matching_documents_tokens

    return documents_


def compute_matching_elements(documents_output_with_average):
    columns = ["Chars/Tokens"]
    aggregated_data = []
    for process_type, process in documents_output_with_average.items():
        process_data = ["Chars (no spaces)"]
        for corpus, documents in process.items():
            if corpus not in columns:
                columns.append(corpus)
            process_data.append(documents['average']['matching_documents_chars_no_spaces'])
        aggregated_data.append(process_data)
        process_data = ["Chars (spaces)"]
        for corpus, documents in process.items():
            if corpus not in columns:
                columns.append(corpus)
            process_data.append(documents['average']['matching_documents_chars_spaces'])
        aggregated_data.append(process_data)
        process_data = ["Tokens"]
        for corpus, documents in process.items():
            process_data.append(documents['average']['matching_documents_tokens'])
        aggregated_data.append(process_data)

    return aggregated_data


def compute_differences(document_output_with_average):
    columns = ["Process type"]
    aggregated_data = []
    for process_type, process in documents_output_with_average.items():
        process_data = ["Chars (no spaces)"]
        for corpus, documents in process.items():
            if corpus not in columns:
                columns.append(corpus)
            process_data.append(documents['average']['diff_chars_no_spaces'])
        aggregated_data.append(process_data)
        process_data = ["Chars (spaces)"]
        for corpus, documents in process.items():
            if corpus not in columns:
                columns.append(corpus)
            process_data.append(documents['average']['diff_chars_spaces'])
        aggregated_data.append(process_data)
        process_data = ["Tokens"]
        for corpus, documents in process.items():
            process_data.append(documents['average']['diff_tokens'])
        aggregated_data.append(process_data)

    return aggregated_data


def print_largest_differences(documents_output):
    for process_type, process in documents_output.items():
        print(process_type)
        for corpus, documents in process.items():
            print(f"\t{corpus}")
            sorted_by_diff = sorted(
                documents['processed'].items(),
                key=lambda x: x[1]['stats']['diff_chars_spaces']
            )

            sorted_by_diff_tokens = sorted(
                documents['processed'].items(),
                key=lambda x: x[1]['stats']['diff_tokens']
            )

            output_neg = [f"\n\t\t\t -{item[0]}: {item[1]['stats']['diff_chars_spaces']}" for item in
                          sorted_by_diff[:2]]
            print("".join(output_neg))
            output_pos = [f"\n\t\t\t -{item[0]}: {item[1]['stats']['diff_chars_spaces']}" for item in
                          sorted_by_diff[-2:]]
            print("".join(output_pos))
            # print(f"Files to check:\n {[item[0] for item in sorted_by_diff_tokens[:2]]}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare two PDFAlto runs.")
    parser.add_argument('--run1', required=True, help='Path to first PDFAlto output directory')
    parser.add_argument('--run2', required=True, help='Path to second PDFAlto output directory')
    parser.add_argument('--sorted-differences', action='store_true',
                        help='Find the greatest differences in characters and tokens between the two runs')
    args = parser.parse_args()

    pdfalto_A = args.run1
    pdfalto_B = args.run2

    documents_output = {}
    documents_output["standard"] = compute_run_statistics(pdfalto_A, pdfalto_B)
    documents_output_with_average = compute_averages(documents_output)
    matching = compute_matching_elements(documents_output_with_average)
    diff = compute_differences(documents_output_with_average)


    def print_markdown_table(title, data):
        print(f"\n## {title}\n")
        # Assume first row contains headers
        headers = [str(h) for h in data[0]]
        print("| " + " | ".join(headers) + " |")
        print("|" + "---|" * len(headers))
        for row in data[1:]:
            print("| " + " | ".join(str(cell) for cell in row) + " |")


    # Prepare matching and diff tables with headers
    matching_table = [
                         ["Metric"] + list(documents_output_with_average["standard"].keys())
                     ] + matching
    diff_table = [
                     ["Metric"] + list(documents_output_with_average["standard"].keys())
                 ] + diff

    print_markdown_table("Matching Documents", matching_table)
    print_markdown_table("Differences (Averages)", diff_table)

    if args.sorted_differences:
        print_largest_differences(documents_output)