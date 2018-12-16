import datetime
from flask import render_template, request, Blueprint
from blog.models import Post

main = Blueprint('main',__name__)

today = datetime.date.today()
a = today.replace(year=today.year+1)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)
    
@main.route("/about")
def about():
    return render_template('about.html',title='About', date=today ,a = a)
