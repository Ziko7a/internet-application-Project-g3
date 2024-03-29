from flask import Flask, render_template
from json import dumps
from postdata import posts
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

app.config['MAIL_USERNAME'] = 'foodrecipes.ubt@gmail.com'
app.config['MAIL_PASSWORD'] = 'hejdqutdxmvjvgzb'

mail = Mail(app)

@app.route('/send-email')
def send_email():
    msg = Message('Hello', sender='foodrecipes.ubt@gmail.com', recipients=['recipient@example.com'])
    msg.body = "This is a test email sent from Flask!"
    mail.send(msg)
    return "Email sent!"


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact-us")
def contact():
    return render_template('contact-us.html')

@app.route("/americanfoods")
def american():
    return render_template('americanfoods.html')

@app.route("/chinesefood")
def chinese():
    return render_template('chinesefood.html')

@app.route("/saudifoods")
def saudi():
    return render_template('saudifoods.html')

@app.route("/mobile")
def mobile():
    return render_template('mobile.html')

@app.route("/reqres-data")
def reqres():
    return render_template('reqres-data.html')


@app.route("/json_posts")
def json_posts():
    data = {
        'data': posts,
        'total': len(posts)
    }
    return dumps(posts)

@app.route("/posts")
def posts():
    return render_template('post-all.html',
                           title='all posts',
                           posts=posts)

@app.route('/postsingle')
def postSingle():
    return render_template('post-single.html', posts=posts)

@app.route('/post/3')
def postsingle():
    post = next((p for p in posts if p['id'] == 3), None)
    if post:
        return render_template('post-all.html', post=post)
    else:
        return "Post not found."
    
@app.route('/posts/<int:post_id>')
def show_post(post_id):
    if post_id < len(posts):
       p = posts[post_id]
       return render_template('post-single.html',
       title= f"Post#{post_id}", p = p )
    else:
        return render_template('404.html'), 404


@app.errorhandler(404)
def err_404(error):
   return render_template( '404.html' ), 404

if __name__ == '__main__':
    app.run(debug=True)