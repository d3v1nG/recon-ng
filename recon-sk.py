#!/usr/bin/env python3

import sys
# prevent creation of compiled bytecode files
sys.dont_write_bytecode = True
from recon.core import base
from recon.core.framework import Colors
import subprocess
import json

# recon-ng / recon-cli wrapper class
class recon_sk():
    
    def __init__(self, filepath):
        # get information from config into memory
        self.config = self.get_config(file)
        self.workspace = self.config['workspace']
        self.domains = self.config['domains']
        self.keys = self.config['keys']
        self.modules = self.config['modules']
        self.reporting = self.config['reporting']
        self.framework = base.Recon()
        options = [base.Mode.CLI]
        options.append(self.workspace)
        self.framework.start(*options)

    # util to show workspace dash
    def show_dashboard(self):
        cmd = "dashboard"
        print(cmd)
        self.framework.onecmd(cmd)

    # gets everything needed from config in memory
    def get_config(self, filepath):
        file = open(filepath, 'r')
        config = json.load(file)
        file.close() 
        return config

    # add api keys to workspace
    def add_api_keys(self):
        for key in self.keys:
            cmd = "keys add {0} {1}".format(key, self.keys[key])
            self.framework.onecmd(cmd)

    def add_options(self):
        for domain in self.domains:
            self.framework.insert_domains(domain)
        self.framework.insert_companies(self.workspace)


    # runs modules from config
    def run_all_modules(self):
        for mod in self.modules:
            print("[~] Running module "+mod)
            self.run_module(mod)

    # actual module execution
    def run_module(self, name):
        mod = self.framework._do_modules_load(name)
        # if no module found return 
        if not mod: return
        mod.do_run(None)
        for table in mod._summary_counts:
            new_hosts = mod._summary_counts[table]['new']
            if new_hosts > 0:
                print("[+] New hosts found, run modules again.")
                return True

    def run_report_modules(self):
        for r in self.reporting:
            print("[~] Reporting")
            self.run_module(r)

if __name__ == "__main__":
    arg = sys.argv
    file = arg[1]

    session = recon_sk(file)
    session.add_api_keys()
    session.add_options()
    session.run_all_modules()
    session.show_dashboard()
    session.run_report_modules()