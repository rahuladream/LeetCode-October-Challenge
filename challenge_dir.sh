n=1;
max=31;
while [ "$n" -le "$max" ]; do
  mkdir "Day$n"
  n=`expr "$n" + 1`;
done
