#  JavaScript Restrictor is a browser extension which increases level
#  of security, anonymity and privacy of the user while browsing the
#  internet.
#
#  Copyright (C) 2019  Libor Polcak
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

param (
	[Parameter(Position=0)]
	[String]
	$file
)

$WRAPPING = ""
Get-ChildItem ".\common" -Filter wrapping*.js | Sort-Object |
Foreach-Object {
    $WRAPPING += "`"$_`","
}
$WRAPPING = $WRAPPING.TrimEnd(',')
$WRAPPING += "`n"

(Get-Content $file).replace("WRAPPING", $WRAPPING) | Set-Content $file -Encoding "UTF8"
