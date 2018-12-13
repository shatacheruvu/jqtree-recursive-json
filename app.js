const getJSON = uri => fetch(uri).then(response => response.json());
const isObject = value => typeof value === "object" && value !== null;

const addNode = (parent, key, value) => {
  const child = {};
  if (isObject(value)) {
    child["name"] = key;
    child["children"] = [];
  } else {
    child["name"] = key + ": " + value;
  }
  parent.push(child);
  console.log(parent);
  return parent;
};

const build = (parent, data) => {
  let counter = 0;
  Object.keys(data).forEach(key => {
    parent = addNode(parent, key, data[key]);
    if (isObject(data[key])) {
      const parent_n = parent[counter]["children"];
      parent[counter]["children"] = build(parent_n, data[key]);
    }
    counter += 1;
  });
  return parent;
};

const generateTree = async data => {
  const parent = [];
  const tree = await build(parent, data);
  $("#tree").tree({ data: tree, keyboardSupport: true, openedIcon: '-', closedIcon: '+'});
};

getJSON("./sample.json").then(generateTree).catch(error => console.error(error));
