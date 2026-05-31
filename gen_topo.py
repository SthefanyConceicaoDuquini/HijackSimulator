import os

if not os.path.exists('configs'):
    os.makedirs('configs')

def generate_bird_conf(asn, router_id, neighbors):
    conf = f"""
log stderr all;
debug protocols all;
router id {router_id};

protocol device {{ }}
protocol direct {{ ipv4; }}
protocol kernel {{ ipv4 {{ export all; }}; }}

"""
    for n_asn, n_ip in neighbors:
        conf += f"""
protocol bgp peer_{n_asn} {{
    local as {asn};
    neighbor {n_ip} as {n_asn};
    ipv4 {{
        import all;
        export all;
    }};
}}
"""
    return conf

topo = {
    "AS1": {"id": "1.1.1.1", "neighbors": [(2, "10.99.0.3")]},
    "AS2": {"id": "2.2.2.2", "neighbors": [(1, "10.99.0.2")]}
}

for as_name, data in topo.items():
    with open(f"configs/{as_name}.conf", "w") as f:
        f.write(generate_bird_conf(as_name.replace("AS", ""), data["id"], data["neighbors"]))
