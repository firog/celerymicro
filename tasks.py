from celery import Celery
import subprocess
import os

rabbitmqservice = os.environ.get('RABBITMQ_SERVICE_SERVICE_HOST')

celery = Celery('tasks', backend='rpc://', broker='amqp://guest:guest@%s:5672//' % rabbitmqservice)

#celery.conf.result_backend = 'sqlite:///'

#celery.conf.update(CELERY_RESULT_BACKEND = 'db+sqlite:///results.sqlite',)
@celery.task(name='app.tasks.fileContent')
def fileContent():
    fastafile = '/saves/newfa.fa'
    file_content = []
    with open(fastafile, 'r') as f:
        for n in range(50):
        # for line in f:
            d = {'read_id':'', 'read': ''}
            d['read_id'] = f.readline().rstrip()
            d['read'] = f.readline().rstrip()
            file_content.append(d)
    return file_content


@celery.task(name='app.tasks.fib')
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)

@celery.task(name='app.tasks.wherami')
def wherami():
    return ((subprocess.check_output(["pwd"])).decode('UTF-8')).rstrip('\n')


@celery.task
def blast_task(filename,outfmt,blastn,block,evalue):
    wherami = ((subprocess.check_output(["pwd"])).decode('UTF-8')).rstrip('\n')
    scripts_path = wherami+'bashscripts'

    # filename.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

    filename = wherami+'/userUploads/newfa.fa'
    subprocess.call(['/myapp/makeblastdb','-in',filename,'-dbtype','nucl','-out',filename+'db'])
    subprocess.call(['%s/bashscripts/runparallelblast.sh' % wherami ,filename, block, "/myapp/"+blastn, evalue, outfmt, filename+'db'])


####### @celery.task(name='app.tasks.caw_task')
####### def caw_task(cawform):
#######     form = cawform
#######     if form.validate_on_submit():
#######         f = form.zipfile.data
#######         filename = secure_filename(f.filename)
#######         f.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
#######         return redirect(url_for('tools.caw'))
#######     return render_template('tools/caw.html', form=form)


@celery.task(name='app.tasks.test_uptask')
def test_uptask(f):
	filename = secure_filename(f.filename)
	f.save('/saves', filename)
	return '200'


@celery.task(name='app.tasks.upload_task')
def upload_task(dataFile, save_path):
    # dataFile.save(save_path)
    # filename.save(save_path)

    # form = UploadForm()
	# if form.validate_on_submit():
	# 	f = form.uploadFile.data
	# 	filename = secure_filename(f.filename)
	# 	f.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
	# 	return render_template('pages/index.html')
	# return render_template

    pass
    # f = request.files['file']
    # filename = secure
    #
    #
    #
    # def upload_file():
    # 	if request.method == 'POST':
    # 		f = request.files['file']
    # 		filename = secure_filename(f.filename)
    # 		f.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
    # 		flash('File uploading.')
    # 		return render_template('pages/index.html')

