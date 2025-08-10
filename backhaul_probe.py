import json, argparse, time, random, os
import pandas as pd
os.makedirs('reports', exist_ok=True)

def simulate_latency(path):
    # Dummy numbers to mimic backhaul hops
    base = 3 if path=='wired' else 8
    jitter = [random.uniform(0,4) for _ in range(60)]
    return [base + j for j in jitter]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--topology', default='docs/topology.json')
    ap.add_argument('--out', default='reports/backhaul_latency.csv')
    args = ap.parse_args()
    topo = json.load(open(args.topology))
    rows = []
    for sat in topo['satellites']:
        series = simulate_latency(sat['uplink'])
        for i, v in enumerate(series):
            rows.append({'node': sat['name'], 'uplink': sat['uplink'], 't': i, 'lat_ms': round(v,2)})
    pd.DataFrame(rows).to_csv(args.out, index=False)
    print('Saved', args.out)

if __name__=='__main__':
    main()
