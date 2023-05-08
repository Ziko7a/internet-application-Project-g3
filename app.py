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

@app.route("/contact")
def contact():
    return render_template('contact-us.html')

@app.route("/american")
def american():
    return render_template('americanfoods.html')

@app.route("/chinese")
def chinese():
    return render_template('chinesefood.html')

@app.route("/saudi")
def saudi():
    return render_template('saudifoods.html')

@app.route("/mobile")
def mobile():
    return render_template('mobile.html')

@app.route("/reqres")
def reqres():
    return render_template('reqres-data.html')

@app.route ("/post/<int:post_id>")
def post (post_id):
    post = posts[post_id]
    return render_template ('post.html]',title=post['title'], p=post)

@app.route("/json_posts")
def json_posts():
    data = {
        'data': posts,
        'total': len(posts)
    }
    return dumps(posts)

@app.route('/postall')
def postall():
    return render_template('post-all.html', posts=posts)

@app.route('/postsingle')
def postSingle():
    return render_template('post-single.html', posts=posts)

@app.route('/post/3')
def postsingle():
    post = next((p for p in posts if p['id'] == 3), None)
    if post:
        return render_template('post-single.html', post=post)
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

