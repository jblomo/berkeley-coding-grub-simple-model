# Example: Simple model for Berkeley Coding for Grub challenge

This produces a simple model: it uses the training data to record the average
stars for a business.  To make a hypothesis about a new review, it just uses the
average for that business.

## Usage

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ zcat yelp_academic_dataset.json.gz | python simple-model-generator.py > hypothesis.py
    $ python simple-model.py < test_reviews.json > hypothesis.json
    $ curl -Fhypothesis=@hypothesis.json http://yelp-csua-coding.herokuapp.com/rmse

## Resources

http://www.yelp.com/academic_dataset

test_reviews.json available to Berkeley students during the competition

To test results http://yelp-csua-coding.herokuapp.com/rmse

## License

Copyright 2009-2012 Yelp (Jim Blomo jim.blomo@yelp.com)

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
