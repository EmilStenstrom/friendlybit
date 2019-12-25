---
id: 943
title: Hur säkra är svenska banker? (Swedish)
date: 2015-03-01T19:22:05
author: Emil Stenström
excerpt: Säkerheten varierar stort bland svenska banker. Bankens storlek hänger inte ihop med hur väl dom hanterar säkerheten. Ingen av de fyra storbankerna kom med på topplistan. Några små banker finns med i toppen, några riktigt stora finns i botten.
layout: post
guid: http://friendlybit.com/?p=943
permalink: /security/hur-sakra-ar-svenska-banker/
categories:
  - Security
---
_Säkerheten varierar stort bland svenska banker. Bankens storlek hänger inte ihop med hur väl dom hanterar säkerheten. Ingen av de fyra storbankerna kom med på topplistan. Några små banker finns med i toppen, några riktigt stora finns i botten._

För att testa bankernas säkerhet gav jag varje bank två olika betyg:

1. **Kryptering: Krypteras trafiken mellan dig och banken ordentligt?**

   Utan kryptering kan andra se de uppgifter som du skickar till banken, personnummer, lösenord, och koder. Dessa relativt tekniska tester görs med hjälp av [SSL Labs](https://www.ssllabs.com/ssltest/). Betygsskalan kommer direkt från SSL Labs och går från A-F, där A är bäst. Notera att jag testar inloggningssidan, inte startsidan.

2. **Visuellt: Ser allt ok ut i webbläsaren?**

   Det finns gott om guider som lär ut webbsäkerhet till ovana användare. Här tittar jag på om banksajterna är konfigurerade så att allt ser OK ut för en vanlig användare. Har sajten grönt hänglås? Jag har använt samma betygsskala: A-F, där A är bäst.

Bankerna kommer från Finansinspektionens lista över [bankaktiebolag och medlemsbanker](http://www.fi.se/Templates/InstitutcategoriesPage.aspx?id=2466?la=sv). De lokala sparbankerna har inte tagits med, och inte heller de som främst riktar sig till företag. Testet gjordes 2015-02-28. [Rådata för testet finns här](https://docs.google.com/spreadsheets/d/1KBwhyUt9Afo7_4p0izS8eSudGyHr89Ckwym--pNe1S4/edit?usp=sharing), inklusive länkarna till SSL Labs där du kan se testresultatet själv.

### Uppdaterat:

Eftersom denna artikel fått väldigt bra spridning har flera av bankerna hört av sig. Ofta med konkreta förbättringar de har genomfört på grund av min artikel. Här hittar du en tidslinje över hur artikeln har ändrats över tid.

  * 2015-03-03: **Inga fler uppdateringar görs från detta datum och framåt...**
  * 2015-03-02: **Danske Bank** tillagd. Dom får tyvärr bara ett C.
  * 2015-03-02: Kontrollerade stöd för [**DNSSEC**](https://en.wikipedia.org/wiki/Domain_Name_System_Security_Extensions): Landshypotek, Marginalen, Danske Bank, och Länsförsäkringar är de enda som stödjer det.
  * 2015-03-03: Rättade felaktig klassificering av SBAB. Jag hade testat startsidans certifikat, inte inloggningssidans.
  * 2015-03-04: **SBAB Bank** har förbättrat sitt certifikat på startsidan.
  * 2015-03-04: **Länsförsäkringar** har uppdaterat sitt certifik och får nu ett B.
  * 2015-03-05: **Ekobanken** har uppdaterat sitt certifikat och får nu ett A.
  * 2015-03-05: **Forex bank** har uppdaterat sitt certifikat och får nu ett A.
  * 2015-03-05: **Santander Consumer** har släppt en ny internetbank och hamnar nu på B.
  * 2015-03-06: **MedMera Bank** har uppdaterat sitt certifikat och får nu ett B.
  * 2015-03-07: **Carnegie Bank** har uppdaterat sitt certifikat och får nu ett A
  * 2015-03-08: **SBAB Bank** har gjort ytterligare uppdateringar och blir första bank med A/A. Full pott!
  * 2015-03-12: **JAK Medlemsbank** har uppdaterat sitt certifikat och får nu ett B.
  * 2015-03-12: **Länsförsäkringar** har uppdaterat sitt certifikat och får nu ett A-.
  * 2015-03-18: **Swedbank** kör nu HTTPS på sin startsida.
  * 2015-04-11: **Resurs Bank** har uppdaterat certifikatet på sin startsida, och kräver nu även https där. Inloggningscertifikatet kommer att uppdateras också, men är inte klart ännu.
  * 2015-04-24: **Skandiabanken** kör nu HTTPS på sin startsida.
  * 2015-10-28: **Resurs Bank** har flyttat sin inloggningssida till egen domän och certifikat.

## Bankerna med bäst säkerhet (A):

Fantastiska resultat för alla dessa fyra banker. Krypteringen uppfyller best practices och du kan sova gott med vissheten att din bank är bland Sveriges bästa.

<table>
  <tr>
    <th rowspan="2">
    </th>
    <th colspan="2">
      Kryptering
    </th>
    <th colspan="2">
      Visuellt
    </th>
  </tr>
  <tr>
    <th>
      Betyg
    </th>
    <th>
      Not
    </th>
    <th>
      Betyg
    </th>
    <th>
      Not
    </th>
  </tr>

  <tr>
    <td>
      <strong>SBAB</strong>
    </td>
    <td>
      <strong>A</strong>
    </td>
    <td>
      1
    </td>
    <td>
      <strong>A</strong>
    </td>
    <td>
    </td>
  </tr>

  <tr>
    <td>
      <strong>Skandiabanken</strong>
    </td>
    <td>
      <strong>A</strong>
    </td>
    <td>
      1
    </td>
    <td>
      <strong>A</strong>
    </td>
    <td>
    </td>
  </tr>

  <tr>
    <td>
      <strong>Resurs Bank</strong>
    </td>
    <td>
      <strong>A</strong>
    </td>
    <td>
      1
    </td>
    <td>
      <strong>A</strong>
    </td>
    <td>
    </td>
  </tr>

  <tr>
    <td>
      <strong>Landshypotek</strong>
    </td>
    <td>
      <strong>A</strong>
    </td>
    <td>
      2
    </td>
    <td>
      <strong>B</strong>
    </td>
    <td>
      4
    </td>
  </tr>

  <tr>
    <td>
      <strong>Carnegie Investment Bank</strong>
    </td>
    <td>
      <strong>A</strong>
    </td>
    <td>
    </td>
    <td>
      <strong>B</strong>
    </td>
    <td>
      4
    </td>
  </tr>

  <tr>
    <td>
      <strong>Ekobanken</strong>
    </td>
    <td>
      <strong>A</strong>
    </td>
    <td>
    </td>
    <td>
      <strong>B</strong>
    </td>
    <td>
      4
    </td>
  </tr>

  <tr>
    <td>
      <strong>Forex Bank</strong>
    </td>
    <td>
      <strong>A</strong>
    </td>
    <td>
    </td>
    <td>
      <strong>B</strong>
    </td>
    <td>
      4
    </td>
  </tr>

  <tr>
    <td>
      <strong>Länsförsäkringar Bank</strong>
    </td>
    <td>
      <strong>A-</strong>
    </td>
    <td>
      3
    </td>
    <td>
      <strong>A</strong>
    </td>
    <td>
    </td>
  </tr>

  <tr>
    <td>
      <strong>Marginalen Bank</strong>
    </td>
    <td>
      <strong>A-</strong>
    </td>
    <td>
      3
    </td>
    <td>
      <strong>A</strong>
    </td>
    <td>
    </td>
  </tr>

  <tr>
    <td>
      <strong>Nordnet</strong>
    </td>
    <td>
      <strong>A-</strong>
    </td>
    <td>
      3
    </td>
    <td>
      <strong>A</strong>
    </td>
    <td>
    </td>
  </tr>
</table>

**Noter**:

  1. Grattis till **SBAB Bank, Skandiabanken** och **Resurs Bank** som får A i båda kategorier.
  2. En extra eloge till **Landshypotek** som får noll varningar från SSL Labs.
  3. Flera banker får **A minus** eftersom de saknar stöd för [Forward Secrecy](https://en.wikipedia.org/wiki/Forward_secrecy). Förenklat innebär det att krypteringsmetoden ändras över tid, så att någon som avlyssnat trafik till en sajt för länge sedan inte kan dekrypteras den om sajten hackas senare. Totalt har endast tre svenska banker har stöd för detta (Landshypotek, Skandiabanken och ICA Banken (se nedan)). Bra jobbat!
  4. Flera bankers **startsidor saknar kryptering**. Eftersom inloggningssidorna är krypterade är detta inte katastrof, bara olyckligt. Att ha kryptering på hela sin webbplats är en bra idé eftersom kunden vänjer sig vid att se det [gröna hänglåset](https://support.google.com/chromebook/answer/95617) så länge dom har med banken att göra.

## Bankerna som nästan kom med på topplistan (B):

Även här får bankerna bra betyg. Anledningen att dom missar topplistan är att samtliga banker i denna lista har problem med vilka krypteringsalgoritmer/protokoll dom stödjer. Det är enkelt egentligen: Om en krypteringsmetod är bevisat osäker (t.ex. RC4 eller SSL3) ska den plockas bort. Att ha den kvar innebär att kunderna luras att tro att deras uppkoppling mot banken är säker trots att den inte är det.

<table>
  <tr>
    <th rowspan="2">
    </th>
    <th colspan="2">
      Kryptering
    </th>
    <th colspan="2">
      Visuellt
    </th>
  </tr>

  <tr>
    <th>
      Betyg
    </th>
    <th>
      Not
    </th>
    <th>
      Betyg
    </th>
    <th>
      Not
    </th>
  </tr>

  <tr>
    <td>
      <strong>ICA Banken</strong>
    </td>
    <td>
      <strong>B</strong>
    </td>
    <td>
      1
    </td>
    <td>
      <strong>A</strong>
    </td>
    <td>
    </td>
  </tr>

  <tr>
    <td>
      <strong>Avanza</strong>
    </td>
    <td>
      <strong>B</strong>
    </td>
    <td>
    </td>
    <td>
      <strong>A</strong>
    </td>
    <td>
    </td>
  </tr>

  <tr>
    <td>
      <strong>MedMera Bank</strong>
    </td>
    <td>
      <strong>B</strong>
    </td>
    <td>
    </td>
    <td>
      <strong>A</strong>
    </td>
    <td>
    </td>
  </tr>

  <tr>
    <td>
      <strong>Santander Consumer</strong>
    </td>
    <td>
      <strong>B</strong>
    </td>
    <td>
    </td>
    <td>
      <strong>A</strong>
    </td>
    <td>
    </td>
  </tr>

  <tr>
    <td>
      <strong>JAK Medlemsbank</strong>
    </td>
    <td>
      <strong>B</strong>
    </td>
    <td>
    </td>
    <td>
      <strong>A</strong>
    </td>
    <td>
    </td>
  </tr>

  <tr>
    <td>
      <strong>Swedbank</strong>
    </td>
    <td>
      <strong>B</strong>
    </td>
    <td>
    </td>
    <td>
      <strong>A</strong>
    </td>
    <td>
    </td>
  </tr>

  <tr>
    <td>
      <strong>SEB</strong>
    </td>
    <td>
      <strong>B</strong>
    </td>
    <td>
    </td>
    <td>
      <strong>B</strong>
    </td>
    <td>
      2
    </td>
  </tr>

  <tr>
    <td>
      <strong>Volvofinans Bank</strong>
    </td>
    <td>
      <strong>B</strong>
    </td>
    <td>
    </td>
    <td>
      <strong>B</strong>
    </td>
    <td>
      2
    </td>
  </tr>

  <tr>
    <td>
      <strong>Ikanobanken</strong>
    </td>
    <td>
      <strong>B</strong>
    </td>
    <td>
    </td>
    <td>
      <strong>B</strong>
    </td>
    <td>
      2
    </td>
  </tr>

  <tr>
    <td>
      <strong>Nordea Bank AB</strong>
    </td>
    <td>
      <strong>B</strong>
    </td>
    <td>
    </td>
    <td>
      <strong>B</strong>
    </td>
    <td>
      2
    </td>
  </tr>

  <tr>
    <td>
      <strong>Handelsbanken</strong>
    </td>
    <td>
      <strong>B</strong>
    </td>
    <td>
    </td>
    <td>
      <strong>B</strong>
    </td>
    <td>
      2
    </td>
  </tr>
</table>

**Noter**:

  1. **ICA Banken** är nästan med i topplistan ovan. Dom krypterar sin startsida, dom stödjer [Forward Secrecy](https://en.wikipedia.org/wiki/Forward_secrecy), och är dessutom den enda bank som stödjer [HTTP Strict Transfer Security](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security). Tyvärr används krypteringsalgoritmen [RC4](https://en.wikipedia.org/wiki/RC4#Security), en algoritm som inte är säker alls. Har du en lite äldre webbläsare kan du alltså bli lurad att allt ser bra ut, trots att trafiken mellan dig och banken relativt enkelt kan avlyssnas. ICA Banken borde helt enkelt stänga av stöd för RC4, be sina användare att uppgradera sin webbläsare, och inta toppositionen i denna lista.
  2. Flera bankers **startsidor saknar kryptering**. Eftersom inloggningssidorna är krypterade är detta inte katastrof, bara olyckligt. Att ha kryptering på hela sin webbplats är en bra idé eftersom kunden vänjer sig vid att se det [gröna hänglåset](https://support.google.com/chromebook/answer/95617) så länge dom har med banken att göra.

## Bankerna som du borde vara orolig för (C):

Någonstans här är det dags att börja bli orolig. Dessa banker har gemensamt att dom inte hanterar sin kryptering på rätt sätt. Extra olyckligt är det ställt för OK-Q8 Bank som använder en [färdig produkt från EDB](https://nettbank.edb.com/) och ändå får sämst betyg av C-bankerna.

<table>
  <tr>
    <th rowspan="2">
    </th>
    <th colspan="2">
      Kryptering
    </th>
    <th colspan="2">
      Visuellt
    </th>
  </tr>

  <tr>
    <th>
      Betyg
    </th>
    <th>
      Not
    </th>
    <th>
      Betyg
    </th>
    <th>
      Not
    </th>
  </tr>

  <tr>
    <td>
      <strong>Danske Bank</strong>
    </td>
    <td>
      <strong>B</strong>
    </td>
    <td>
    </td>
    <td>
      <strong>F</strong>
    </td>
    <td>
      2
    </td>
  </tr>

  <tr>
    <td>
      <strong>Erik Penser</strong>
    </td>
    <td>
      <strong>C</strong>
    </td>
    <td>
      3
    </td>
    <td>
      <strong>F</strong>
    </td>
    <td>
      4, 5
    </td>
  </tr>

  <tr>
    <td>
      <strong>OK-Q8 Bank</strong>
    </td>
    <td>
      <strong>C</strong>
    </td>
    <td>
      3
    </td>
    <td>
      <strong>F</strong>
    </td>
    <td>
      1, 4, 6
    </td>
  </tr>
</table>

**Noter:**

  1. OK-Q8 Bank lyckas vända något bra &#8211; det gröna hänglåset &#8211; till något mindre bra. Ett klick på det gröna hänglåset visar vem som garanterar säkerheten på webbplatsen. Bakom OK-Q8 Bank står EVRY AS, **ett norskt bolag, som garant**.Hur ska en kund veta att det är banken som står bakom det certifikatet, att dom har kommit till rätt sajt? Underkänt.
  2. Danske Bank har bara har satsat på en **grått hänglås**. Den gråa hänglåset betyder att uppkopplingen är krypterad, men inte vem som står bakom den (så kallad [Extended Validation](https://en.wikipedia.org/wiki/Extended_Validation_Certificate)). För något så känsligt som banktjänster ska ett riktigt EV-certifikat användas.
  3. Flera banker verkar inte ha skyddat sig från ett **säkerhetshål som döpts till [POODLE](https://community.qualys.com/blogs/securitylabs/2014/10/15/ssl-3-is-dead-killed-by-the-poodle-attack)**. Google publicerade detaljer om hur man använder sig av hacket redan i oktober 2014. Att det fortfarande finns banker som inte skyddat sig är anmärkningsvärt.
  4. Flera bankers **startsidor saknar kryptering**. Eftersom inloggningssidorna är krypterade är detta inte katastrof, bara olyckligt. Att ha kryptering på hela sin webbplats är en bra idé eftersom kunden vänjer sig vid att se det [gröna hänglåset](https://support.google.com/chromebook/answer/95617) så länge dom har med banken att göra.
  5. Erik Penser gör kapitalfel på sin inloggningssida, den **ser inte ut att vara krypterad**. Som kund ska man aldrig skriva in känsliga inloggningsuppgifter på en webbsida som saknar hänglås. Erik Penser gör visserligen rätt bakom kulisserna (inloggningssidan ÄR krypterad) men det visas inte upp för kunden alls. Gör om, gör rätt.
  6. OK-Q8 Bank och Danske Bank visar inte något som helst hänglås i webbläsaren. Anledningen är att inloggningssidan **hämtar bilder över en helt okrypterad uppkoppling**. Det gör att man väldigt lätt kan se att du loggar in på banken. Danske Bank döljer dessutom denna miss genom att visa inloggningssidan i en popupruta. Riktigt illa.

## Bankerna du borde undvika (F):

Dags för bottennoteringarna. Det gemensamma för dessa banker är att dom har allvarliga problem med sin kryptering. Du kan därför inte kan lita på att trafiken till deras sajter är ordentligt krypterad.

**Inga banker ligger på den här positionen längre. Bra jobbat av alla fem!**

## Slutligen

Det finns väldigt många andra kriterier att sätta betyg på, men jag nöjer mig med detta denna gång. Kanske finns det någon annan som vill fortsätta jämförelsen på sin egen blogg?

Vill du diskutera resultaten vidare finns jag på Twitter: @[EmilStenstrom](http://twitter.com/EmilStenstrom)
