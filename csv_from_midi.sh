for f in ./midi/*.mid
do
	midicsv $f $f.csv
	mv ./midi/*.csv ./csv/
done
