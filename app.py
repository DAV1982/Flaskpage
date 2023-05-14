from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Band

app = Flask(__name__)

engine = create_engine('sqlite:///band-list.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/posts')
def posts():
    articles = Band.query.order_by(Band.date.desc()).all()
    return render_template("posts.html", articles=articles)


@app.route('/posts/<int:id>')
def posts_detail(id):
    article = Band.query.get(id)
    return render_template("posts_detail.html", article=article)


@app.route('/posts/<int:id>/del')
def posts_delete(id):
    article = Band.query.get_or_404(id)

    try:
        session.delete(article)
        session.commit()
        return redirect('/posts')
    except:
        return "Article's delete error"


@app.route('/feedback')
def feedback():
    return render_template("feedback.html")


@app.route('/posts/<int:id>/update', methods=['POST', 'GET'])
def post_update(id):
    article = Band.query.get(id)
    if request.method == "POST":
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']

        try:
            session.commit()
            return redirect('/posts')
        except:
            return "Article's update error"

    else:
        article = Band.query.get(id)
        return render_template("post_update.html", article=article)


@app.route('/create-article', methods=['POST', 'GET'])
def create_article():
    article = Band.query.get(id)
    if request.method == "POST":
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']

        article = Band(title=article.title, intro=article.intro, text=article.text)

        try:
            session.add(article)
            session.commit()
            return redirect('/posts')
        except:
            return "Article's edit error"

    else:
        return render_template("create-article.html")


if __name__ == "__main__":
    app.run(debug=True)
