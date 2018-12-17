push:
	git push origin master

serve:
	mkdocs serve

publish:
	git push origin master
	mkdocs gh-deploy
