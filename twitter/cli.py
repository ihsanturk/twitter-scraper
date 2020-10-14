"""ihsan-twitter - Twitter scraper with stream feature.

Usage:
  twitter search <query> [-l]

  -l --latest        Sort by latest tweets instead of top.
  -h --help          Show this screen.
  -v --version       Show version.

"""
import twitter
from docopt import docopt

def main():
	args = docopt(__doc__, version='0.0.1')
	twtr = twitter.Twitter(args['--latest'])
	print(twtr.search(args['<query>']))
