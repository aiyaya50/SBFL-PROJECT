package com.gzoltar.sfl.formulas;

public final class F1 extends AbstractSFLFormula{
	 @Override
 	 public String getName() {
 	 return "F1";
 	}
 	 @Override
 	 public double compute(final double n00, final double n01, final double n10, final double n11) {
 	 	 try { 
 	 	 return Math.pow(n11,2)*(-n10*(n00 + n11) - n11*(n00 + n01 + n10 + n11))/(n00 + n01 + n10 + n11); 
 	 	 }
 	 	 catch(ArithmeticException e){
 	 	 	 return 0.0; 
 	 	 }
 	 	 
 	 }
}
