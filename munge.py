import pandas
messages = pandas.read_csv('./crowdflower-corporate-messaging/Corporate-messaging-DFE.csv', encoding='iso8859_2')
dialogues = messages[messages.category == 'Dialogue']
pandas.set_option('max_colwidth', 140)
link_dialogues = dialogues[dialogues.text.str.match('.*http.*')]
