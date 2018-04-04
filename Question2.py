import Classes as Cls
import SupportTransientState as STS

# expected rewards from 1000 games

setOfGames = Cls.SetOfGames(id=1, prob_head=0.5, n_games=1000)
outcomes = setOfGames.simulation()

setOfGames2 = Cls.SetOfGames(id=2, prob_head=0.45, n_games=1000)
outcomes2 = setOfGames2.simulation()

STS.print_comparative_outcomes(outcomes, outcomes2)
