## awk tutorial

### Exercise: What if you wanted just the sum column, and didn't need the original table? Write an awk command that takes a two column table and outputs just the sum column.

```bash
    paste <(seq 1 5) <(seq 11 15) | awk '{$3 = $1 + $2; print $3}'
```

### Exercise: Write a python program stats-sum which reads a newline-separated list of floating-point numbers from standard input. When it reaches the end of standard input, it prints the sum, and exits.

The [stats-sum](stats-sum) file

```bash
    seq 1 5 | ./stats-sum
    15.0
```

### Exercise: Write similar "aggregator" programs computing stats-mean, stats-median, stats-variance, stats-stddev (standard deviation), stats-mad (median absolute deviation). Feel free to use the standard library, but do not use any third-party python packages.

The programs are: [stats-mean](stats-mean), [stats-median](stats-median), [stats-variance](stats-variance), [stats-stddev](stats-stddev) and [stats-mad](stats-mad)


### Exercise: Write a program stats; this program reads standard input and takes arguments. The arguments it takes are aggregations "mean", "median", "variance", etc. The standard input is a numeric table with tab as the column separator and newline as the record separator. The nth column is fed to the nth aggregator program via popen; the results are printed as a single record.

```
    paste <(seq 1 10) <(seq 1 10) <(seq 1 10) | ./stats mean median variance
    5.5	5.5	9.166667
```

### Exercise: What are the benefits of this multiple-communicating-programs architecture? What are the drawbacks? Explain.
In this case, as many resources as necessary (or possible) are engaged (e.g. 3 cores) thus computing everything in parallel rather than one after the other. As for the drawbacks, it is important to limit the number of process and leave

### Exercise: What happens if your columns are different lengths? Are empty cells treated as zero? If so, change the design by altering the stats program to skip empty cells.

Replace `inputs = line.strip().split('\t')` with `inputs = [x if x else "0" for x in line.strip().split('\t')]`

### Exercise: Explain how you might change the design to permit more than one aggregation of a single column. How would you communicate this to stats with arguments? What logic needs to be changed in stats? Do you need to change the aggregator programs at all?

paste <(seq 1 10) <(seq 1 10) <(seq 1 10) | ./stats bundle mean median variance

### Exercise: Explain how you might change the design to permit more than one aggregation of a single column. How would you communicate this to stats with arguments? What logic needs to be changed in stats? Do you need to change the aggregator programs at all?

One of the agruments has to specify if a single aggregation or a bundle of them has to be applied. e.g.

```
    paste <(seq 1 10) | ./stats1 all mean median variance
```

or

```
    paste <(seq 1 10) <(seq 1 10) <(seq 1 10) | ./stats1 single mean median variance
```

The first argument would indicate 

It is not necessary to update aggregator programs, as they can run in parallel on the same data, e.g. additional subprocess

Exercise: Explain how you might change the design to permit two-column aggregators, for example, integration. How would you communicate this to stats with arguments? What logic needs to be changed in stats?

stdin is split by tabs. To permit two column aggregators, the split has to go reflect this, e.g. no split at all if there are two-column input or split by 2 if the input is Nx2-column

Exercise: Choose one of these two design changes, and implement it. If you choose the two-column aggregators: the formula for integral is the sum of the expression (after the data 
is sorted by the first column)

Design change 1:

[.stats1](stats1) - an additional parameter specifies if all aggregators have to apply to the first (only, others are skipped) column or each to a separate one.