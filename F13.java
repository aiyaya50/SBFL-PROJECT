package com.gzoltar.sfl.formulas;

public final class F13 extends AbstractSFLFormula{
	 @Override
 	 public String getName() {
 	 return "F13";
 	}
 	 @Override
 	 public double compute(final double n00, final double n01, final double n10, final double n11) {
 	 	 try { 
 	 	 return n10*(n00 + n11)/(n00 + n01 + n10 + n11); 
 	 	 }
 	 	 catch(ArithmeticException e){
 	 	 	 return 0.0; 
 	 	 }
 	 	 
 	 }
}
