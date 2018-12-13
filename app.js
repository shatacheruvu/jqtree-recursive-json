const getJSON = uri => fetch(uri).then(response => response.json());
const isObject = value => typeof value === "object" && value !== null;

const buildNode = (key, value, hasChildren) => {
  const node = {};
  if (hasChildren) {
    node["name"] = key;
    node["children"] = [];
  } else {
    node["name"] = `${key}: ${value}`;
  }
  return node;
};

const addNode = (parent, key, value) => {
  const node = isObject(value)
    ? buildNode(key, value, hasChildren = true)
    : buildNode(key, value, hasChildren = false);
  parent.push(node);
  return parent;
};

const buildTree = (parent, data) => {
  let counter = 0;
  Object.keys(data).forEach(key => {
    parent = addNode(parent, key, data[key]);
    if (isObject(data[key])) {
      const parent_n = parent[counter]["children"];
      parent[counter]["children"] = buildTree(parent_n, data[key]);
    }
    counter += 1;
  });
  return parent;
};

const generateTree = async data => {
  const parent = [];
  const tree = await buildTree(parent, data);
  $("#tree").tree({
    data: tree,
    keyboardSupport: true,
    openedIcon: "-",
    closedIcon: "+"
  });
};

getJSON("./sample.json")
  .then(generateTree)
  .catch(error => console.error(error));
