from datetime import datetime, timedelta

NOW = datetime.now()


class Promo:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        print('\n--- init ---')
        print(self.name)
        print(self.date)
        print('--- end init ---\n\n')

    def out(self):
        print('--- out ---')
        print(self.name)
        print(self.date)
        print('---end out ---\n\n')

    @property
    def expired(self):
        return self._expired

    @expired.setter
    def expired(self):
        self._expired = bool(NOW < self.date)

#        if NOW < self.date:
#            print('NOW < self.date')
#            return False
#        else:
#            print('else')
#            return True
    pass

    def var_test(self):
        print(NOW)
        print(self.date)

if __name__ == '__main__':
    past_time = NOW - timedelta(seconds=3)
    future_date = NOW + timedelta(days=3)

    twitter_promo = Promo('twitter', past_time)
    newsletter_promo = Promo('newsletter', future_date)
    assert twitter_promo.expired
    assert newsletter_promo.expired

