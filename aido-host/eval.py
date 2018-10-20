#!/usr/bin/env python
import multiprocessing
import os
import subprocess
import sys
import time

from duckietown_challenges import wrap_evaluator, ChallengeEvaluator, ChallengeInterfaceEvaluator


def start_server(cie):
    cwd = '/amod/target'
    cp = 'amod-1.5.2.jar'
    fn = os.path.join(cwd, cp)
    if not os.path.exists(fn):
        msg = 'Could not find %s.' % cp
        msg += '\nThese are the files: %s' % list(os.listdir(cwd))
        raise Exception(msg)
    cmd = ['java', '-Xmx10000m', '-cp', cp, 'amod.aido.AidoHost']
    cie.debug('Running in %s: %s' % (cwd, cmd))
    subprocess.check_call(cmd, cwd=cwd, stderr=sys.stderr, stdout=sys.stdout)
    cie.debug('Finished start_server() thread')


class Evaluator(ChallengeEvaluator):

    def prepare(self, cie):
        assert isinstance(cie, ChallengeInterfaceEvaluator)

        self.p = multiprocessing.Process(target=start_server, args=(cie,))
        self.p.start()

        cie.info('Waiting 5 seconds until host is up')
        time.sleep(5)
        cie.info('now going to solution')

        cie.set_challenge_parameters({})

    def score(self, cie):
        assert isinstance(cie, ChallengeInterfaceEvaluator)
        cie.debug('waiting for server to finish')
        self.p.join()
        cie.debug('creating report')
        cmd = ['prince', '/amod/target/output/001/report/report.html',
               '-o', '/report.pdf']
        subprocess.check_call(cmd, cwd='/', stderr=sys.stderr, stdout=sys.stdout)
        cie.set_evaluation_file('report.pdf', '/report.pdf')

        files = [
            'aidoScores1and2Intg.png',
            'aidoScores1and2Diff.png',
            'numberCustomersPlot.png',
            'requestsPerDriveTime.png',
            'requestsPerTotalTravelTime.png',
            'requestsPerWaitTime.png',
            'statusDistribution.png',
            'occAndDistRatios.png',
            'stackedDistance.png',
            'distanceDistribution.png',
            'binnedWaitingTimes.png',
            'aidoScoresIntg/aidoScoresIntg.csv',
            'aidoScoresIncr/aidoScoresIncr.csv',
        ]

        for fn in files:
            full = os.path.join('/amod/target/output/001/data', fn)
            cie.set_evaluation_file(os.path.basename(fn), full)

        cie.set_score('passed', True)


if __name__ == '__main__':
    wrap_evaluator(Evaluator())
