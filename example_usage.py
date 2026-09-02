from client import RealtimeSearchRerankingCitationGrounderClient

def main():
    client = RealtimeSearchRerankingCitationGrounderClient()
    res = client.ground_and_rerank_citations('High temperature superconductor discoveries', 20, 5)
    print('Search Citation Grounder: ' + res['grounding_run_id'])
    print('Rerank Score: ' + str(res['cross_encoder_rerank_score']) + ' | Hallucination Suppression: ' + str(res['hallucination_suppression_index_pct']) + '%')
    print('Citations Count: ' + str(res['verified_grounded_citations_count']))
    print('Attribution URL: ' + res['attributed_markdown_synthesis_url'])

if __name__ == '__main__':
    main()
