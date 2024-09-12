
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}


document.addEventListener('DOMContentLoaded', function () {
    // Создаем экземпляр Intersection Observer
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.1 // Настроить порог видимости, при котором срабатывает анимация
    });

    // Наблюдаем за всеми элементами с классом 'service-item'
    document.querySelectorAll('.service-item').forEach(item => {
        observer.observe(item);
    });
});
document.addEventListener("DOMContentLoaded", () => {
    const elements = document.querySelectorAll(".fade-in");
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    elements.forEach(element => {
        observer.observe(element);
    });
});
document.addEventListener("DOMContentLoaded", () => {
    const elements = document.querySelectorAll(".fade-in");
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    elements.forEach(element => {
        observer.observe(element);
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const doctorItems = document.querySelectorAll('.doctor-item');

    function checkVisibility() {
        const windowHeight = window.innerHeight;
        const scrollY = window.scrollY;

        doctorItems.forEach(item => {
            const itemTop = item.getBoundingClientRect().top + scrollY;

            if (scrollY + windowHeight > itemTop) {
                item.classList.add('visible');
            }
        });
    }

    window.addEventListener('scroll', checkVisibility);
    checkVisibility(); // Проверить видимость при загрузке страницы
});

document.addEventListener('DOMContentLoaded', function() {
    const button = document.querySelector('.schedule-button');

    function handleScroll() {
        const rect = button.getBoundingClientRect();
        if (rect.top < window.innerHeight && rect.bottom > 0) {
            button.classList.add('show');
            window.removeEventListener('scroll', handleScroll); // Удалить обработчик после анимации
        }
    }

    window.addEventListener('scroll', handleScroll);
    handleScroll(); // Проверить сразу при загрузке страницы
});
