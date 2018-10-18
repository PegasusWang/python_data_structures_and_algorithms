push:
	git push origin master

serve:
	make serve

publish:
	git push origin master
	mkdocs gh-deploy

