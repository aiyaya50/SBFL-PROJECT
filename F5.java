package com.gzoltar.sfl.formulas;

public final class F5 extends AbstractSFLFormula{
	 @Override
 	 public String getName() {
 	 return "F5";
 	}
 	 @Override
 	 public double compute(final double n00, final double n01, final double n10, final double n11) {
 	 	 try { 
 	 	 return n11; 
 	 	 }
 	 	 catch(ArithmeticException e){
 	 	 	 return 0.0; 
 	 	 }
 	 	 
 	 }
}
