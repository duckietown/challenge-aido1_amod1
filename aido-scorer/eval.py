#!/usr/bin/env python

from duckietown_challenges import wrap_evaluator, ChallengeEvaluator, ChallengeInterfaceEvaluator


class Scorer(ChallengeEvaluator):

    def prepare(self, cie):
        assert isinstance(cie, ChallengeInterfaceEvaluator)

        cie.set_challenge_parameters({})

    def score(self, cie):
        assert isinstance(cie, ChallengeInterfaceEvaluator)

        cie.set_score('passed2', True)


if __name__ == '__main__':
    wrap_evaluator(Scorer())
