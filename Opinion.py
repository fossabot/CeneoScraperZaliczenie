import requests
from bs4 import BeautifulSoup

class Opinion:

    def __init__(self, id, author, recommendation, stars, 
                content, pros, cons, useful, useless, purchased,
                review_date, purchase_date):
        self.id = id
        self.author = author
        self.recommendation = recommendation
        self.stars = stars
        self.content = content
        self.pros = pros
        self.cons = cons
        self.useful = useful
        self.useless = useless
        self.purchased = purchased
        self.review_date = review_date
        self.purchase_date = purchase_date
    
    def __repr__(self):
        return f"{{id={self.id},\
    author={self.author},\
    recommendation={self.recommendation},\
    stars={self.stars},\
    content={self.content},\
    pros={self.pros},\
    cons={self.cons},\
    useful={self.useful},\
    useless={self.useless},\
    purchased={self.purchased},\
    review_date={self.review_date},\
    purchase_date={self.purchase_date}}}"

    @staticmethod
    def get_opinion_feature(opinion, tag, tag_class, child=None):
        try:
            if child:
                return opinion.find(tag, tag_class).find(child).get_text().strip()
            else:
                return opinion.find(tag, tag_class).get_text().strip()
        except AttributeError:
            return None
