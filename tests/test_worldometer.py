# -*- coding: utf-8 -*-
""" tests module
"""
import pytest

from covid import Covid

covid = Covid("worldometers")


def test_all_data():
    data = covid.get_data()
    assert data is not None
    assert type(data) == list
    element = data[0]
    assert "country" in element
    assert "confirmed" in element
    assert "total_cases" in element
    assert "active" in element
    assert "active_cases" in element
    assert "deaths" in element
    assert "recovered" in element
    assert "new_cases" in element
    assert "new_deaths" in element
    assert "critical" in element
    assert "new_deaths" in element
    assert "total_tests" in element
    assert "total_tests_per_million" in element
    assert "total_cases_per_million" in element
    assert "total_deaths_per_million" in element
    assert "population" in element


def test_get_by_country_name():
    element = covid.get_status_by_country_name("sweden")
    assert type(element) is dict
    assert "country" in element
    assert "confirmed" in element
    assert "total_cases" in element
    assert "active" in element
    assert "active_cases" in element
    assert "deaths" in element
    assert "recovered" in element
    assert "new_cases" in element
    assert "new_deaths" in element
    assert "critical" in element
    assert "new_deaths" in element
    assert "total_tests" in element
    assert "total_tests_per_million" in element
    assert "total_cases_per_million" in element
    assert "total_deaths_per_million" in element
    assert "population" in element
    assert element["country"] == "Sweden"


def test_get_by_country_invalid_name():
    with pytest.raises(ValueError):
        covid.get_status_by_country_name("USA-A")


def test_total_active_cases():
    data = covid.get_total_active_cases()
    assert type(data) is int


def test_total_confirmed_cases():
    data = covid.get_total_confirmed_cases()
    assert type(data) is int


def test_total_deaths():
    data = covid.get_total_deaths()
    assert type(data) is int


def test_total_recovered():
    data = covid.get_total_recovered()
    assert type(data) is int


def test_list_countries():
    countries = covid.list_countries()
    assert type(countries) == list
