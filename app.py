from flask import Flask, render_template, request, redirect, url_for
import csv


app= Flask("my flask app!")

@app.route('/home')
def home():
	return render_template("index.html")

@app.route('/blog/<id>/')
def blog(id):
	return "<h1>Showing blog no. </h1>" + id

@app.route('/bio')
def mybio():
	name = request.args.get('name')
	age = request.args.get('age')
	names=['a', 'b', 'c']
	return render_template("index.html", name=name, age=age, names=names)

@app.route('/upload', methods=['GET', 'POST'])
def upload_data():
	if request.method=='GET':
		return render_template('upload.html')
	else:
		name = request.form.get('name')
		age = request.form.get('age')
		branch = request.form.get('branch')

		with open("student_db.csv", "a") as f:
			writer= csv.writer(f)
			writer.writerow([name, age, branch])

		"""Alternative
		with open("student_db.csv", "a") as f:
			writer= csv.Dictwriter(f, fieldnames=["name", "age", "branch"]) 	_check
			writer.writerow(request.form)
		"""

		image = request.files.get('image')
		image.save('static/images/'+image.filename)
		return redirect(url_for('home'))


if __name__=="__main__":
	app.run(host="0.0.0.0", port=7000, use_reloader=True)


	"""myenv\Scripts\activate"""