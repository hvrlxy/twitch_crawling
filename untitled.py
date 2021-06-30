from tensortrade.environments import TradingEnvironment

# a trading stretegy composed of 2 features: trading env and agents

#exchange: live or simulate
from tensortrade.exchanges.simulated import FBMExchange
exchange = FBMExchange(base_instrument='UTC', timeframe='1h')

#feature pipelines:
from tensortrade.features import FeaturePipeline
from tensortrade.feature.scalers import MinMaxNormalizer
from tensortrade.feature.stationarity import FractionalDifference
from tensortrade.feature.indicators import SimpleMovingAverage

price_columns = ["open", "high", "low", "close"]
normalize_price = MinMaxNormalizer(price_columns)
moving_averages = TAlibIndicator(["EMA", "RSI", "BB"]) #choose indicators
difference_all = FractionalDifference(difference_order=0.6)
feature_pipeline = FeaturePipeline(steps=[normalize_price,
                                          moving_averages,
                                          difference_all])

exchange.feature_pipeline = feature_pipeline

#Action Scheme: turn agent's actions into executable trades
from tensortrade.actions import DiscreteActions

action_scheme = DiscreteActions(n_actions=20, instrument='BTC')

# reward: -1 for not holding a trade, 1 for holding a trade, 
# 2 for purchasing an instrument and a value corresponding to the profit
from tensortrade.rewards import SimpleProfit
reward_scheme = SimpleProfit()

# trading env has 4 feature: exchange, action_scheme, reward_scheme, (optional) feature pipeline
environment = TradingEnvironment(exchange=exchange,
								action_scheme=action_scheme,
								reward_scheme=reward_scheme,
								feature_pipeline=feature_pipline)

# Learning agent : we choose a model(PPO2) and a policy (MlpLstmPolicy) 
# for out RL algorithms
from stable_baselines.common.policies import MlpLnLstmPolicy
from stable_baselines import PPO2

model = PPO2
policy = MlpLnLstmPolicy
params = { "learning_rate": 1e-5 }

agent = model(policy, environment, model_kwargs=params)

# combine trading environment and learning agent to get a trading strategy
from tensortrade.strategies import TensorforceTradingStrategy, StableBaselinesTradingStrategy

strategy = StableBaselinesTradingStrategy(environment=environment,
										model=PPO2,
										policy=MlpLnLstmPolicy,
										model_kwargs=params)

performance=strategy.run(steps=10000,
						episode_callback=stop_early_callback)



