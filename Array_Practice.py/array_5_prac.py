num = [["kajol",[1,2,3,4,5],["Mayuri",["Hello","My","Name","Is","Ketan"],[True, False],((1,"Jayes"))]]]
print(num[0][2][2][1])


data = [["Rahul", [10,20,30,40], ["Pune", ["Python","SQL","Git"], [True,False], (5,"Amit")]]]
print(data[0][1][2]) #30
print(data[0][2][1][1]) #SQL
print(data[0][2][2][1]) #false
print(data[0][2][3][1]) #amit


data = [["Neha", [11,22,33,44], ["Mumbai", ["Red","Green","Blue"], [False,True], (10,"Raj")]]]
print(data[0][1][3]) #44
print(data[0][2][1][1]) # green
print(data[0][2][2][0]) #false
print(data[0][2][3][1]) #raj


data = [["Ketan", [100,200,300], ["Nashik", ["Hello","My","Name","Is","Ketan"], [True,False], (1,"Jay")]]]  
print(data[0][1][1]) #200
print(data[0][2][1][2]) #name
print(data[0][2][2][1]) #False
print(data[0][2][3][1]) #jay


data = [["Pooja", [5,10,15,20], ["Delhi", ["Data","Science","Python"], [False,True], (2,"Riya")]]]
print(data[0][1][2]) #15
print(data[0][2][1][1]) #science
print(data[0][2][2][0]) #false
print(data[0][2][3][1]) #riya

data = [["Amit", [1,3,5,7,9], ["India", ["I","Love","Python"], [True,False], (50,"Om")]]]
print(data[0][2][1][2]) #python
print(data[0][2][3][1]) #om
print(data[0][2][0]) #india
print(data[0][1][4]) #9

data = [
    [
        "Sneha",
        [12, 24, 36, 48],
        [
            "Nashik",
            ["Learn", "Code", "Practice"],
            [False, True],
            (99, "Aryan")
        ]
    ]
]

print(data[0][1][2]) #36
print(data[0][2][1][1])#code
print(data[0][2][2][1])#true
print(data[0][2][3][0])#99

data = [
    [
        "Rahul",
        [10, 20, 30, 40],
        [
            "Pune",
            ["Python", "NumPy", "Pandas"],
            [True, False],
            (85, "Sneha")
        ]
    ]
]

print(data[0][2][2][1])#false
print(data[0][1][3])#40
print(data[0][2][3][0])#85
print(data[0][2][0])#pune


data = [
    [
        "Ketan",
        [
            10,
            20,
            [30, 40, [50, 60, [70, 80]]]
        ],
        (
            "Python",
            [
                "NumPy",
                "Pandas",
                ["SQL", "ML", ["AI", "DL"]]
            ],
            {
                "city": "Nashik",
                "marks": [80, 90, [95, 100, [105, 110]]]
            }
        )
    ],

    [
        "Jayesh",
        [
            120,
            130,
            [140, 150, [160, 170, [180, 190]]]
        ],
        (
            "Java",
            [
                "Spring",
                "Hibernate",
                ["JDBC", "Servlet", ["Maven", "JSP"]]
            ],
            {
                "city": "Pune",
                "marks": [60, 70, [75, 85, [88, 92]]]
            }
        )
    ],

    [
        "Rahul",
        [
            200,
            210,
            [220, 230, [240, 250, [260, 270]]]
        ],
        (
            "C++",
            [
                "STL",
                "OOP",
                ["DSA", "Pointers", ["Stack", "Queue"]]
            ],
            {
                "city": "Mumbai",
                "marks": [65, 75, [80, 85, [90, 95]]]
            }
        )
    ]
]

print(data[2][0])#rahul
print(data[2][2][2]["marks"][2][1])#85
print(data[1][2][1][2][0])#jdbc
print(data[1][2][0])#java




data = [
    [
        "Akash",
        [14, 24, 34, 44],
        [
            "nashik",
            ["Code", "Debug", "Test"],
            [True, False],
            (95, "Vikas")
        ]
    ]
]


print(data[0][0])#akash
print(data[0][1][2])#34
print(data[0][2][0])#nashik
print(data[0][2][1][1])#debug
print(data[0][2][2][1])#false



data = [
    [
        "Snehal",
        [18, 28, 38, 48],
        [
            "Delhi",
            ["Learn", "Practice", "Improve"],
            [False, True],
            (89, "Pooja")
        ]
    ]
]

print(data[0][0])#snehal
print(data[0][2][0])#delhi
print(data[0][2][3][1])#pooja
print(data[0][1][3])#48

