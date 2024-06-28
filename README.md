



Salam.

# Bu məlumat setində bu sorgulara cavab tapmışam : 
1. İstehsal həcminə görə Top20 də olan məsulların illər üzrə dəyişimini regresiyon analizi və qrafik olaraq göstərmişəm.[1992-2022]
2. iki zaman intervalında(Mən 1992-1996,2017-2022 seçmişəm) istehsal olunmuş məsulların statistiki olarak məna əlaqəsinin olub olmadığını yoxlanılıb.(T-test)
3. İnflyasiyanın illər üzrə istehsala təsiri.


# Proyektin şeması : 

<<<<<<< HEAD
 --| analysis_of_production_data
 -------| data
 -----------|  Azerbaijan_crops_and_livestocs_products.csv
 -----------| Azerbaijan_Value_of_Agricultural_Production.csv
 -----------| inflation_azerbaijan.csv
 -------| impact_inflation_prod.ipynb
 -------| ttest.ipynb
 -------| regression_and_trend_analysis.ipynb
 -------| README.md
=======
---| analysis_of_production_data \n
--------| data
------------|  Azerbaijan_crops_and_livestocs_products.csv
------------| Azerbaijan_Value_of_Agricultural_Production.csv
------------| inflation_azerbaijan.csv
--------| impact_inflation_prod.ipynb
--------| ttest.ipynb
--------| regression_and_trend_analysis.ipynb
--------| README.md
>>>>>>> 78f8a3a88beff2d72f36e03d416f3ac312f588e9





 # Sütun adlarının mənaları : 

| Sahənin adı  | Mənası       |
|:------------:|:-------------:|
| Domain Code  | Sahənin kodu  |
| Domain      | Sahənin adı   |
|Area Code (M49) | M49 standartına görə ölkə kodu |
|Area | Ölkənin adı |
|Element Code | Ölçülmüş dəyişənin adı |  
| Element  |Ölçülmüş dəyişənin spesifik kodudur |
| Item Code (CPC) | Məhsulun kodu |
| Item | Məhsulun adı |
| Year Code | İl kodu.
| Year | İstehsal olunan ili bildirir |
| Unit |Dəyəri ölçəcəyimiz kəmiyyət |
| Value | Dəyərin özü.
|Flag | Məlumatın güvənirliyinə dair kateqoriyanın baş hərfi ilə işarəsidir |
|Flag Description | Məlumatın güvənirliyinə dair kateqoriyanın açıqlamasıdır |
| Note  | Əlavə açıqlamaları bildirir |



# Açıqlamaya ehtiyac olunan sətirlərlərdə olan dəyərlər  : 
Məlumatın necə toplanmasındakı qaynaqların izahı(Flag Description) : 
| Qaynağın adı | Mənası   |
|:------------:|:--------:|
| Imputed value | Statistiki olaraq təxmin edilən verilənlər |
| Estimated value | Bəzi fərziyyələr üzərinə qurulmuş modeldən təxmin edilən verilənlər |
| Unofficial value | Rəsmi olmayan mənbələrdən alınan məlumatlar |
| Missing value (data cannot exist, not applicable) | Mövcud olmayan verilənlər |
| Official figure | Rəsmi mənbələrdən alınan məlumatlar |



| Sahənin adı | Mənası |
|:-----------:|:-------:|
| Area harvest | Aid olduğu məhsulun istehsal sahəsinin ölçüsü |
| Yield  | Məhsuldarlığı |
| Production | İstehsal miqdarı |
| Stocs | Sayı(ədədlə) |
| Yield/carcass weight |  Karkazın ağırlığı |
| Producing Animals/Slaughtered | Kəsilə bilən heyvanların istehsalı |


Asses --- Ölkədə olan eşşəklərin sayısı.(Sayısı Value hissəsində)
inflation_rate --- İnflyasiya dərəcəsi



### Gross Production Value (current thousand SLC)
**Açıqlama:**
- Bu dəyər istehsalın pul qarşılığını cari qiymətlərlə ifadə edir.(current -indiki,constant - sabit,inflyasiyasız)
- "SLC" (Local Currency), Cari pulu təmsil edir  .

Məhsulların istehsalına inflyasiyanın təsiri \(_{2020}\) = Gross Production Value (current thousand SLC)\(_{2020}\) \(\times\) (1 + İnflyasiya dərəcəsi\(_{2020}\))




# Mənbə : 
Məlumat setinin mənbəyi : World Data Bank(inflation_azerbaijan)

Məlumat setinin mənbəyi :Birləşmiş Millətlər Təşkilatının Ərzaq və Kənd Təsərrüfatı Qurumu (Food and Agriculture Organization of the United Nations) https://www.fao.org/(other csv documents)

