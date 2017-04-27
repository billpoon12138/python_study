


public class MyMath {

	public int my_abs(int x){
		if(x >= 0){
			return x;
		}else{
			return -x;
		}
	}

	public String get_subString(){
		String str = "AA(BB(CC)DD)EE";
		
		int beginIndex = str.indexOf("(");
		int endIndex = str.lastIndexOf(")");
/*		
		System.out.println(beginIndex);
		System.out.println(endIndex);
*/
		String subStr = str.substring(beginIndex +1, endIndex);

		System.out.println(subStr);	

		return subStr;	
	}

}
