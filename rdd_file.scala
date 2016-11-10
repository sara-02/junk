val fnames: List[String] = List(<file1>,<file2>...<fileN>)
var path: String = "hdfs://sandbox:9000/user/root/my_test"

for (fname <- fnames):
{
 val f = sc.textFile(s"$path/$f").collect(); println(s"File >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>: $f"); f.foreach(println)}
}