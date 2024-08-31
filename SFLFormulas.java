/**
 * Copyright (C) 2020 GZoltar contributors.
 * 
 * This file is part of GZoltar.
 * 
 * GZoltar is free software: you can redistribute it and/or modify it under the terms of the GNU
 * Lesser General Public License as published by the Free Software Foundation, either version 3 of
 * the License, or (at your option) any later version.
 * 
 * GZoltar is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even
 * the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser
 * General Public License for more details.
 * 
 * You should have received a copy of the GNU Lesser General Public License along with GZoltar. If
 * not, see <https://www.gnu.org/licenses/>.
 */
package com.gzoltar.sfl;

import com.gzoltar.sfl.formulas.Anderberg;
import com.gzoltar.sfl.formulas.Barinel;
import com.gzoltar.sfl.formulas.DStar;
import com.gzoltar.sfl.formulas.ISFLFormula;
import com.gzoltar.sfl.formulas.Ideal;
import com.gzoltar.sfl.formulas.Jaccard;
import com.gzoltar.sfl.formulas.Kulczynski2;
import com.gzoltar.sfl.formulas.Naish1;
import com.gzoltar.sfl.formulas.Ochiai;
import com.gzoltar.sfl.formulas.Ochiai2;
import com.gzoltar.sfl.formulas.Opt;
import com.gzoltar.sfl.formulas.RogersTanimoto;
import com.gzoltar.sfl.formulas.RusselRao;
import com.gzoltar.sfl.formulas.SBI;
import com.gzoltar.sfl.formulas.SimpleMatching;
import com.gzoltar.sfl.formulas.SorensenDice;
import com.gzoltar.sfl.formulas.Tarantula;
import com.gzoltar.sfl.formulas.Fo1;
import com.gzoltar.sfl.formulas.Fo2;
import com.gzoltar.sfl.formulas.Fo3;
import com.gzoltar.sfl.formulas.Fo4;
import com.gzoltar.sfl.formulas.Fo5;
import com.gzoltar.sfl.formulas.Fo6;
import com.gzoltar.sfl.formulas.Fo7;
import com.gzoltar.sfl.formulas.Fo8;
import com.gzoltar.sfl.formulas.Fo9;
import com.gzoltar.sfl.formulas.Fo10;
import com.gzoltar.sfl.formulas.Sgf_1;
import com.gzoltar.sfl.formulas.Fo12;
import com.gzoltar.sfl.formulas.Fo13;
import com.gzoltar.sfl.formulas.Fo14;
import com.gzoltar.sfl.formulas.Fo15;
import com.gzoltar.sfl.formulas.Sgf1;
import com.gzoltar.sfl.formulas.Sgf2;
import com.gzoltar.sfl.formulas.Fo16;
import com.gzoltar.sfl.formulas.Fo17;
import com.gzoltar.sfl.formulas.Sgf_2;
import com.gzoltar.sfl.formulas.Fo19;
import com.gzoltar.sfl.formulas.Fo20;
import com.gzoltar.sfl.formulas.Fo21;
import com.gzoltar.sfl.formulas.Fo22;
import com.gzoltar.sfl.formulas.Sgf1;
import com.gzoltar.sfl.formulas.Sgf2;
import com.gzoltar.sfl.formulas.Meco;

public enum SFLFormulas {

  OCHIAI(new Ochiai()),

  OCHIAI2(new Ochiai2()),

  TARANTULA(new Tarantula()),

  JACCARD(new Jaccard()),

  SGF_2(new Sgf_2()),

  SGF_1(new Sgf_1()),

  SBI(new SBI()),

  KULCZYNSKI2(new Kulczynski2()),

  SORENSEN_DICE(new SorensenDice()),

  ANDERBERG(new Anderberg()),

  SIMPLE_MATCHING(new SimpleMatching()),

  ROGERS_TANIMOTO(new RogersTanimoto()),

  RUSSEL_RAO(new RusselRao()),

  DSTAR(new DStar()),
  
  FO1(new Fo1()),
  
  FO2(new Fo2()),
  
  FO3(new Fo3()),
  
  FO4(new Fo4()),
  
  FO5(new Fo5()),
  
  FO6(new Fo6()),
  
  FO7(new Fo7()),
  
  FO8(new Fo8()),
  
  FO9(new Fo9()),
  
  FO10(new Fo10()),
  
  SGF1(new Sgf1()),

  SGF2(new Sgf2()),
  
  FO12(new Fo12()),
  
  FO13(new Fo13()),
  
  FO14(new Fo14()),
  
  FO15(new Fo15()),
  
  FO16(new Fo16()),
  
  FO17(new Fo17()),

  FO19(new Fo19()),
  
  FO20(new Fo20()),
  
  FO21(new Fo21()),
  
  FO22(new Fo22()),
  
  OPT(new Opt()),
  
  BARINEL(new Barinel()),

  IDEAL(new Ideal()),

  NAISH1(new Naish1()),
  
  MECO(new Meco());

  private final ISFLFormula formula;

  private SFLFormulas(final ISFLFormula formula) {
    this.formula = formula;
  }

  public ISFLFormula getFormula() {
    return this.formula;
  }
}
