#!/usr/bin/env python

import json
import operator


def prep_data(file_name):
    """Read a JSON file with people, ages and a list of age brackets and
    prepare the data for further processing.

    Args:
       file_name: The name of the JSON file to prepare.

    Raises:
       IOError: If ''filename'' does not exist or can't be read.

    Returns: A tuple with a list of people sorted by age, and a bracket list
    that includes the age brackets in the file plus the maximum possible age to process.
    """

    with open(file_name, 'r') as json_file:
        json_data = json.load(json_file)
    bracket_list = sorted(json_data['buckets'])
    max_age = max(json_data['ppl_ages'].items(), key=operator.itemgetter(1))[1] + 1
    ppl_sorted = dict(sorted(json_data['ppl_ages'].items(), key=operator.itemgetter(1)))
    bracket_list.append(max_age)
    return ppl_sorted, bracket_list


def print_yaml(ppl_sorted, bracket_list):
    """Print a YAML of age brackets and people that belong to each bracket.
    Results look like:
    0-25:
      - John
      - Tracy
    25-46:
      - Mandy
      - Yang

    Args:
       ppl_sorted: A dictionary of people and ages sorted by age.
       bracket_list: a list of integer age brackets to sort people by.
    """

    curr_min = 0
    i = 0
    curr_max = bracket_list[i]
    print('{}-{}:'.format(curr_min, curr_max))

    for name, age in ppl_sorted.items():
        if (age >= curr_min) and (age < curr_max):
            print('  - ' + name)
        else:
            i += 1
            curr_min = curr_max
            curr_max = bracket_list[i]
            print('{}-{}:'.format(curr_min, curr_max))


def main():
    """Sort a JSON comprised of tuples of people and ages,
    and a list of age brackets, and print out a YAML of people
    sorted to age brackets. People's ages must be equal or higher than the lower limit of
    the bracket and lower than the higher limit of the bracket. Lowest possible age is 0,
    highest possible age is the maximum age given, +1."""

    filename = 'hw.json'
    ppl_ages = prep_data(filename)[0]
    age_brackets = prep_data(filename)[1]
    print_yaml(ppl_ages, age_brackets)


if __name__ == '__main__':
    main()
