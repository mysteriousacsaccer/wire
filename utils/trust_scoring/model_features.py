features_and_pandas_dtypes = {
	# 'n_transactions': 'int',
	'avg_trx_freq': 'float',
	'avg_gas_price': 'float',
	'avg_gas_consumed': 'float',
	'median_sender_nonce': 'float',
	'returning_user_perc': 'float',
	'n_unique_incoming_addresses': 'int',
	'n_deployer_transactions': 'int',
	'contains_abi': 'int',  # Bool, but convert it into 0/1 (1 - True; 0 - False)
	'contains_w3_js': 'int',  # Bool, but convert it into 0/1 (1 - True; 0 - False)
}

feature_weightages = {
	'avg_trx_freq': 8.64769820082531,
	'avg_gas_price': 17.212321412386647,
	'avg_gas_consumed': 11.010181668459143,
	'median_sender_nonce': 11.466813221967087,
	'returning_user_perc': 5.163604743908352,
	'n_unique_incoming_addresses': 7.951081099086453,
	'n_deployer_transactions': 5.032960947712193,
	'contains_abi': 29.383812279865477,
	'contains_w3_js': 4.131526425789332
}

legit_limits = {
	"n_transactions": {"count": 10438.0, "mean": 748.4288177812, "std": 2928.3361215868, "min": 1.0, "25%": 2.0,
					   "50%": 11.0, "75%": 291.0, "max": 184167.0},
	"avg_trx_interval": {"count": 10438.0, "mean": 830977.8996645662, "std": 3705660.6247450579, "min": -1.0,
						 "25%": 357.75, "50%": 32659.4304359146, "75%": 289508.4876592357, "max": 89900314.0},
	"avg_sender_nonce": {"count": 10438.0, "mean": 10155.7224564093, "std": 158433.0195441786, "min": 0.0, "25%": 27.0,
						 "50%": 186.0, "75%": 1022.75, "max": 13762924.0},
	"avg_gas_price": {"count": 10438.0, "mean": 22392603533.3053283691, "std": 287665625916.1614990234,
					  "min": 100000000.0, "25%": 5336560446.5136108398, "50%": 11250830772.4230766296,
					  "75%": 24220919319.4696044922, "max": 29197454919028.640625},
	"avg_gas_consumed": {"count": 10438.0, "mean": 695482.802773325, "std": 1065481.8771862702, "min": 21000.0,
						 "25%": 79623.0066964286, "50%": 260977.1666666667, "75%": 813817.0625,
						 "max": 6956905.4656488551},
	"median_trx_freq": {"count": 8234.0, "mean": 581034.0609667234, "std": 3853874.8664190983, "min": 0.0,
						"25%": 279.25, "50%": 1398.25, "75%": 17005.0, "max": 89900314.0},
	"median_sender_nonce": {"count": 10438.0, "mean": 4330.3177332822, "std": 177314.4668762095, "min": 0.0,
							"25%": 12.0, "50%": 59.0, "75%": 276.5, "max": 15719034.0},
	"median_gas_price": {"count": 10438.0, "mean": 15161470043.7012844086, "std": 19462927146.3669700623, "min": 0.0,
						 "25%": 4000000000.0, "50%": 9000000000.0, "75%": 20000000000.0, "max": 257550000000.0},
	"median_gas_consumed": {"count": 10438.0, "mean": 595709.1461486875, "std": 1097806.8727049755, "min": 14347.0,
							"25%": 45667.25, "50%": 80549.0, "75%": 600032.125, "max": 7775436.5},
	"returning_user_perc": {"count": 10438.0, "mean": 47.0842414675, "std": 37.2652293014, "min": 0.0,
							"25%": 11.8480141246, "50%": 44.4444444444, "75%": 85.7142857143, "max": 100.0},
	"n_unique_incoming_addresses": {"count": 10438.0, "mean": 188.1666027975, "std": 684.3321591878, "min": 1.0,
									"25%": 1.0, "50%": 3.0, "75%": 43.0, "max": 30199.0},
	"n_deployer_transactions": {"count": 10438.0, "mean": 50.6256945775, "std": 324.8757232615, "min": 1.0, "25%": 1.0,
								"50%": 3.0, "75%": 7.0, "max": 7193.0}}

malicious_limits = {
	"n_transactions": {"count": 791.0, "mean": 425.1352718078, "std": 3445.6084260958, "min": 1.0, "25%": 6.0,
					   "50%": 22.0, "75%": 81.0, "max": 84194.0},
	"avg_trx_interval": {"count": 791.0, "mean": 742488.8466147536, "std": 3089047.8218105524, "min": -1.0,
						 "25%": 2222.1599076822, "50%": 23598.8787878788, "75%": 178448.9823270759, "max": 35524555.5},
	"avg_sender_nonce": {"count": 791.0, "mean": 14801.7206068268, "std": 160062.4085582951, "min": 0.0, "25%": 19.0,
						 "50%": 61.0, "75%": 258.0, "max": 3165075.0},
	"avg_gas_price": {"count": 791.0, "mean": 37516960005.2992401123, "std": 34937139262.2576980591,
					  "min": 1000000000.0, "25%": 15001551622.5, "50%": 27143833202.25, "75%": 46789605755.3472213745,
					  "max": 279210870211.0},
	"avg_gas_consumed": {"count": 791.0, "mean": 526383.3127615498, "std": 1348841.9559475398, "min": 21000.0,
						 "25%": 86974.4723502304, "50%": 168289.7826086956, "75%": 352079.5,
						 "max": 15478810.2702702694},
	"median_trx_freq": {"count": 749.0, "mean": 201636.958611482, "std": 1541165.6009489945, "min": 0.0, "25%": 199.0,
						"50%": 775.0, "75%": 3477.5, "max": 33212710.5},
	"median_sender_nonce": {"count": 791.0, "mean": 3718.3400758534, "std": 55836.6786955381, "min": 0.0, "25%": 7.0,
							"50%": 21.5, "75%": 62.0, "max": 1414441.5},
	"median_gas_price": {"count": 791.0, "mean": 33901988556.8482933044, "std": 32406030046.4417037964,
						 "min": 155000000.5, "25%": 11446702352.0, "50%": 22779848143.0, "75%": 43759808042.0,
						 "max": 279210870211.0},
	"median_gas_consumed": {"count": 791.0, "mean": 468184.097977244, "std": 1611546.9627851536, "min": 21000.0,
							"25%": 43988.5, "50%": 58357.0, "75%": 176421.0, "max": 25198759.0},
	"returning_user_perc": {"count": 791.0, "mean": 48.7117099623, "std": 32.4594716626, "min": 0.0, "25%": 25.0,
							"50%": 47.0588235294, "75%": 72.0867208672, "max": 100.0},
	"n_unique_incoming_addresses": {"count": 791.0, "mean": 88.7307206068, "std": 607.7053454516, "min": 1.0,
									"25%": 2.0, "50%": 5.0, "75%": 21.5, "max": 14270.0},
	"n_deployer_transactions": {"count": 791.0, "mean": 21.5044247788, "std": 60.3639985601, "min": 1.0, "25%": 2.0,
								"50%": 4.0, "75%": 15.0, "max": 914.0}}
