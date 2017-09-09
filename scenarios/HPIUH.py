# This sample code helps you get started with the custom scenario API.
#For more details and samples, please see our Documentation
#from dataiku.scenario import Scenario

# The Scenario object is the main handle from which you initiate steps
#scenario = Scenario()

# A few example steps follow

# Building a dataset
#scenario.build_dataset("customers_prepared", partitions="2015-01-03")

# Controlling the train of a dataset
#train_ret = scenario.train_model("uSEkldfsm")
#trained_model = train_ret.get_trained_model()
#performance = get_new_version_metrics().get_performance_values()
#if performance["AUC"] > 0.85:
#    trained_model.activate_new_version()

# Sending custom reports
#sender = scenario.get_message_sender("nnnm", "TryAgain") # A messaging channel
#sender.set_params(sender="sean.hanlon@dataiku.com", recipent="sean.hanlon@dataiku.com")

#sender.send(subject="The scenario is doing well", message="All is good")

from dataiku.scenario import Scenario
scenario = Scenario()

thesender = scenario.get_message_sender("nnnm", "TryAgain (smtp)")

# You can then call send() with message params.
# params are specific to each message channel types

# SMTP mail example
thesender.send(sender="sean.hanlon@dataiku.com", recipient="sean.hanlon@dataiku.com", subject="The scenario is doing well", message="All is good")