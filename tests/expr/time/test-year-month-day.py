#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Copyright 2021 H2O.ai
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#-------------------------------------------------------------------------------
import pytest
from datatable import dt, f
from datatable.time import year, month, day
from datetime import date as d
from tests import assert_equals


def test_year_month_day_simple():
    DT = dt.Frame([d(1970, 1, 2), d(1972, 9, 27), d(2243, 10, 17)])
    RES = DT[:, {"year": year(f[0]), "month": month(f[0]), "day": day(f[0])}]
    assert_equals(RES,
        dt.Frame(year=[1970, 1972, 2243], month=[1, 9, 10], day=[2, 27, 17]))


def test_noargs():
    DT = dt.Frame([None])

    msg = r"Function datatable\.year\(\) requires exactly 1 positional argument"
    with pytest.raises(TypeError, match=msg):
        DT[:, year()]

    msg = r"Function datatable\.month\(\) requires exactly 1 positional argument"
    with pytest.raises(TypeError, match=msg):
        DT[:, month()]

    msg = r"Function datatable\.day\(\) requires exactly 1 positional argument"
    with pytest.raises(TypeError, match=msg):
        DT[:, day()]


def test_invalid_type():
    DT = dt.Frame(range(5))

    msg = r"Function time\.year\(\) requires a date32 column"
    with pytest.raises(TypeError, match=msg):
        DT[:, year(f[0])]

    msg = r"Function time\.month\(\) requires a date32 column"
    with pytest.raises(TypeError, match=msg):
        DT[:, month(f[0])]

    msg = r"Function time\.day\(\) requires a date32 column"
    with pytest.raises(TypeError, match=msg):
        DT[:, day(f[0])]


def test_void_column():
    DT = dt.Frame([None] * 5)
    RES = DT[:, [year(f[0]), month(f[0]), day(f[0])]]
    assert_equals(RES, dt.Frame([[None] * 5] * 3))


def test_nas():
    DT = dt.Frame([d(2001, 5, 17), None, d(2021, 3, 15), None])
    RES = DT[:, {"year": year(f[0]), "month": month(f[0]), "day": day(f[0])}]
    assert_equals(RES,
        dt.Frame(year=[2001, None, 2021, None],
                 month=[5, None, 3, None],
                 day=[17, None, 15, None])
    )
