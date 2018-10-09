#!/usr/bin/env python
import subprocess
import sys

from duckietown_challenges import wrap_solution, ChallengeSolution, ChallengeInterfaceSolution


class Solver(ChallengeSolution):
    def run(self, cis):
        assert isinstance(cis, ChallengeInterfaceSolution)
        cmd = ['java', '-Xmx10000m', '-cp', 'amod-1.4.8.jar', 'amod.aido.demo.AidoGuest', 'aido-host']
        cwd = '/amod/target'
        cis.info('Now running %s' % cmd)

        subprocess.check_call(cmd, cwd=cwd, stdout=sys.stdout, stderr=sys.stderr)

        cis.set_solution_output_dict({})


if __name__ == '__main__':
    wrap_solution(Solver())
