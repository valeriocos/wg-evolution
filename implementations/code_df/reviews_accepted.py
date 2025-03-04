from datetime import datetime

import utils
from pullrequest import PullRequest


class ReviewsAccepted(PullRequest):
    """
    Class for Reviews Accepted
    """

    def compute(self):
        """
        Compute the total number of reviews which were accepted, from the Perceval data.

        :returns count: The total number of reviews accepted
        """

        count = len(self.df['hash'][self.df['merged']].unique())
        return count

    def _agg(self, df, period):
        """
        Perform an aggregation operation on a DataFrame to find
        the total number of reviews accepted in every
        interval of the period specified in the time_series method,
        like 'M', 'W',etc.

        It computes the count of the "category" column of the
        DataFrame for those rows with the 'merge' column having True.

        :param df: a pandas DataFrame on which the aggregation will be
            applied.

        :param period: A string which can be any one of the pandas time
            series rules:
            'W': week
            'M': month
            'D': day

        :returns df: The aggregated dataframe, where aggregations have
            been performed on the "category" column
        """

        df = df[df['merged']]
        df = df.resample(period)['category'].agg(['count'])

        return df


if __name__ == "__main__":
    date_since = datetime.strptime("2018-09-07", "%Y-%m-%d")
    items = utils.read_json_file('../pull_requests.json')

    reviews_accepted = ReviewsAccepted(items)
    print("The total number of reviews accepted is {}"
          .format(reviews_accepted.compute()))

    reviews_accepted = ReviewsAccepted(items, (date_since, None))
    print("The number of reviews created after 2018-09-07 which were accepted is {}"
          .format(reviews_accepted.compute()))

    print("The trends in the number of accepted reviews created"
          " from 2018-09-07 onwards are: ")
    print(reviews_accepted.time_series('M'))
