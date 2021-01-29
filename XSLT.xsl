<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<html> 
<body>
<style>
table, tr, th {  
  border: 1px solid #ddd;
  text-align: left;
  font-family: Tahoma;
}

table {
  border-collapse: collapse;
  width: 50%;
}

tr, td {
  padding: 10px;
}
</style>
  <h2>Movie Collection</h2>
  <table border="1">
    <tr>
      <th bgcolor="C0D6DF"  style="text-align:left">Title</th>
      <th bgcolor="DBE9EE" style="text-align:left">Artist</th>
      <th bgcolor="4a6fa5" style="text-align:left">Rating</th>
      <th bgcolor="166088"  style="text-align:left">Votes</th>
    </tr>
    <xsl:for-each select="Filmy/movie">
    <tr>
      <td><xsl:value-of select="title"/></td>
      <td><xsl:value-of select="rank"/></td>
      <td><xsl:value-of select="rating"/></td>
      <td><xsl:value-of select="votes"/></td>
    </tr>
    </xsl:for-each>
  </table>
</body>
</html>
</xsl:template>
</xsl:stylesheet>

