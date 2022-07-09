import { useState, useEffect } from "reactn";
import axios from "axios";

const PeopleDB = () => {
	const [people, setPeople] = useState([]);
	const [person, setPerson] = useState({
		username: "",
		firstName: "",
		lastName: "",
		age: "",
	});
	const [edit, setEdit] = useState(false);
	const [deleteId, setDeleteId] = useState("");

	useEffect(() => {
		listPeople();
	}, []);

	const listPeople = () => {
		axios
			.get("http://localhost:3333/person")
			.then((res) => {
				setPeople(res.data);
			})
			.catch((err) => {
				console.log(err);
			});
	};

	const addPerson = (person) => {
		axios
			.post("http://localhost:3333/person", person)
			.then((res) => {
				setPeople([...people, res.data]);
			})
			.catch((err) => {
				console.log(err);
			});
	};

	const editPerson = (person) => {
		axios
			.patch("http://localhost:3333/person/" + person._id, person)
			.then((res) => {
				const newPeople = people.map((p) => {
					if (p._id === person._id) {
						return res.data;
					}
					return p;
				});
				console.log(person);
				setPeople(newPeople);
				setEdit(false);
			})
			.catch((err) => {
				console.log(err);
			});
	};

	const deletePerson = (_id) => {
		axios
			.delete("http://localhost:3333/person/" + _id)
			.then((res) => {
				const newPeople = people.filter((p) => p._id !== _id);
				setPeople(newPeople);
			})
			.catch((err) => {
				console.log(err);
			});
	};

	const handleSubmit = (e) => {
		e.preventDefault();

		if (
			person.username === "" ||
			person.firstName === "" ||
			person.lastName === "" ||
			person.age === ""
		) {
			alert("Please fill all fields");
			return;
		} else {
			console.log("submit");
			if (edit) {
				editPerson(person);
			} else {
				addPerson(person);
			}
		}
		setPerson({
			username: "",
			firstName: "",
			lastName: "",
			age: "",
		});
		setEdit(false);
	};

	const handleChange = (e) => {
		setPerson({ ...person, [e.target.name]: e.target.value });
	};

	const handleEdit = (_id) => {
		const person = people.find((person) => person._id === _id);
		setPerson(person);
		setEdit(true);
	};

	const handleDelete = (_id) => {
		setDeleteId(_id);
		setEdit(false);
	};

	const handleDeleteConfirm = () => {
		deletePerson(deleteId);
		setDeleteId("");
	};

	// const logIt = () => {
	// 	let x = Symbol(people);
	// 	let y = Symbol(people);
	// 	let q = { ...x, ...y };
	// 	let z = { ...x, ...y };
	// 	console.log(q);
	// 	console.log(z);
	// 	console.log(x);
	// 	console.log(x === y);
	// };

	return (
		<div className="bg-teal-100 h-screen">
			<h1 className="text-center text-4xl">PeopleDB</h1>
			{/* <button onClick={logIt}>LogIt</button> */}
			<form onSubmit={handleSubmit} className="border-2 border-black">
				<label>Username:</label>
				<input
					type="text"
					name="username"
					value={person.username}
					onChange={handleChange}
					className="border border-black m-1 hover:border-red-500"
				/>
				<label>First Name:</label>
				<input
					type="text"
					name="firstName"
					value={person.firstName}
					onChange={handleChange}
					className="border border-black m-1 hover:border-red-500"
				/>
				<label>Last Name:</label>
				<input
					type="text"
					name="lastName"
					value={person.lastName}
					onChange={handleChange}
					className="border border-black m-1 hover:border-red-500"
				/>
				<label>Age:</label>
				<input
					type="number"
					name="age"
					value={person.age}
					onChange={handleChange}
					className="border border-black m-1 hover:border-red-500"
				/>
				<button
					type="submit"
					className="border rounded-lg border-blue-400 bg-blue-300 hover:bg-blue-800 m-1"
				>
					{edit ? "Update" : "Add"}
				</button>
			</form>
			<ul className="flex flex-wrap">
				{people.map((person) => (
					<li
						key={person._id}
						className={person._id === deleteId ? "border-2 border-red-500" : ""}
					>
						<div className="flex flex-col border border-black w-fit m-2 p-2 items-center">
							<div className="flex flex-row">
								<h1 className=" font-extrabold">User: {person.username}</h1>

								{deleteId === "" && (
									<div>
										<button onClick={() => handleEdit(person._id)}>🛠</button>
										<button onClick={() => handleDelete(person._id)}>💥</button>
									</div>
								)}
								{deleteId && deleteId === person._id && (
									<div className="border-2 border-black w-fit m-1">
										<p>Are you sure you want to delete {person.username}?</p>
										<button onClick={handleDeleteConfirm}>✔</button>
										<button onClick={() => setDeleteId("")}>❌</button>
									</div>
								)}
							</div>
							<div className="flex flex-row">
								<p>First Name: {person.firstName}</p>
							</div>
							<div className="flex flex-row">
								<p>Last Name: {person.lastName}</p>
							</div>
							<div className="flex flex-row">
								<p>Age: {person.age}</p>
							</div>
						</div>
					</li>
				))}
			</ul>
		</div>
	);
};

export default PeopleDB;
