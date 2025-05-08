'use client';
import { useEffect, useState } from "react";



interface Article{
  id: number;
  title: string;
  content: string;
}

export default function Home() {
  const [article, setArticle] = useState<Article[]>([]);
  useEffect(() => {
    fetch("http://127.0.0.1:5000/articles")
    .then(response => response.json())
    .then(data => setArticle(data))
    .catch(error => console.error("Error fetching articles:", error));
  }, []);
console.log(article);

  return (
    <div> Hola mundo</div>
  );
}
