from flask import Flask, request, redirect, render_template

app=Flask(__name__)

@app.route('/mypage/me')
def me():
    return render_template('o_mnie.html')

@app.route('/mypage/contact')
def contact_get():
    return render_template('kontakt.html')

@app.route('/mypage/contact', methods=['POST'])
def contact_post():
    print(request.form)
    return redirect('/mypage/me')