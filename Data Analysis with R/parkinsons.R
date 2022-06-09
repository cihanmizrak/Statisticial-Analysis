library(readxl)
parkinson2 = read_excel("parkinsons.xlsx")

spread = parkinson2$spread2
spread = as.numeric(spread)

ppe = parkinson2$PPE
ppe = as.numeric(ppe)

#normallik testi
#shapiro

spread.norm = shapiro.test(spread)
ppe.norm = shapiro.test(ppe)

if(spread.norm$p.value<0.05 || ppe.norm$p.value<0.05){
  print("değişikenler normal dağılmıyor t testi uygulanamaz")
  
}else{
  #varyans homojenliği testi yapılır
  library(car)
  birlestirilmis.degisken = c(spread.ppe)
  spread.uzunluk = length(spread)
  ppe.uzunluk = length(ppe)
  spread.belirtec = rep(1,spread.uzunluk) # spread uzunlugukadar 1 yaz
  ppe.belirtec = rep(2,ppe.uzunluk)
  
  birlestirilmis.belirtec = c(spread.belirtec,ppe.belirtec)
  test = levene.test(birlestirilmis.degisken,birlestirilmis.belirtec)
  p.degeri = test$'Pr(>F)'[1]
  if (p.degeri<0.05){
    #varyanslar homojen değil iki yanlı t testi
    test = t.test(spread,ppe,var.equal = FALSE)
    #testi değerlendirelim
    if(test$p.value<0.05){
      print("spread verisi ortalaması ile ppe verisinin ortalaması arasında anlamlı bir fark vardır.")
      print(test$p.value)
      
    }else{
      print("Spread verisi ortalaması ile ppe verisi ortalaması arasında istatistiksel olarak anlamlı bir fark yoktur.")
      print(test$p.value)
    }
    #Varyanslar homojen değil tek yönü t testi
    test = t.test(spread,ppe,var.equal = FALSE, alternative = "g")
    if(test$p.value<0.05){
      print("Spread verisi ortalaması ppe verisi ortalamasından büyüktür.")
      print(test$p.value)
    }else{
      print("Spread verisi ortalaması ppe verisi ortalamasından büyük değildir.")
      print(test$p.value)
    }
    #Varyanslar homojen değil tek yönü t testi
    test = t.test(spread,ppe,var.equal = FALSE, alternative = "l")
    if(test$p.value<0.05){
      print("Spread verisi ortalaması ppe verisi ortalamasından küçüktür")
      print(test$p.value)
    }else{
      print("Spread verisi ortalaması ppe verisi ortalamasından küçük değildir.")
      print(test$p.value)
    }
  }else{
    #varyanslar homojen iki yönlü test yapılır. test = t.test(spread,ppe,var.equal = TRUE)
    
    if(test$p.value<0.05){
      print("Spread verisi ortalaması ile ppe verisi ortalaması arasında anlamlı bir fark vardır")
      print(test$p.value)
    }else{
      print("Spread verisi ortalaması ile ppe verisi ortalaması arasında anlamlı bir fark yoktur")
      print(test$p.value)
    }
    #varyanslar homojen tek yönlü test (büyük)
    test = t.test(spread,ppe,var.equal = TRUE,alternative = "g")
    if(test$p.value<0.05){
      print("Spread verisinin ortalaması ppe verisinin ortalamasından büyüktür.")
      print(test$p.value)
      
    }else{
      print("Spread verisinin ortalaması ppe verisinin ortalamasından büyük değildir.")
      print(test$p.value)
    }
    #varyanslar homojen tek yönlü test (küçük)
    test = t.test(spread,ppe,var.equal = TRUE,alternative = "l")
    if(test$p.value<0.05){
      print("Spread verisinin ortalaması ppe verisinin ortalamasından küçüktür.")
      print(test$p.value)
      
    }else{
      print("Spread verisinin ortalaması ppe verisinin ortalamasından küçük değildir.")
      print(test$p.value)
    }
  }
}
