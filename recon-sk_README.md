Usage:
./recon-sk config.json {number of iterations}

If you supply the number of iterations option, the modules will run all the way through, that number of times. default is one iteration.

Config file should be set up as such:
You are able to add as many modules and api keys as you need.

{
    "workspace": "Company",
    "domains": ["companydomain.com"],
    "creator": "Your Name/company",
    "keys": { 
        "key_name": "value",
        "key2_name": "value",
        ...
    },
    "modules": [
        "recon/domains-hosts/bing_domain_api",
        "recon/domains-hosts/brute_hosts",
        ...
    ],
    "reporting": [
        "reporting/csv",
        "reporting/html"
    ]
}
