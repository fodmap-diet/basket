# Food basket
database of foods and their fodmap
 
### Adding item
first clone the basket
```
git clone https://github.com/fodmap-diet/basket.git
```
basket provide an interactive cli tool to add an item
```
python3 tools/add-item.py
```

### Creating Pull Request
we highly encourage pull requests, each pull request will eventually help someone to decide their menu

#### Add items   
##### use cli to add item(s)
items must be added using above method [(Adding item)](https://github.com/fodmap-diet/basket#adding-item)
provided tools ensure the sanitization of input data   

##### format
pull request must be in the below format
```
// state items
Add/Modify item(s):
1. <item>
2. <item>
...

// list each items as:
<item>: 
if changed:
   state the different between previous and new version
if new item:
   state what is added
source: 
   state the sources of the informations
```

#### Resolve issue / Add feature 
##### create an issue
create an issue at [(basket issues)](https://github.com/fodmap-diet/basket/issues)   
Describe the details as   
```
// Issue details 
  // Current behaviour
  // Expected behaviour
```

##### raise PR
raise a pull request with the issue-no at [(basket PRs)](https://github.com/fodmap-diet/basket/pulls)

