using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

/// <summary>
/// Summary description for Class1
/// </summary>
namespace BowlThemUp.Models
{
	public class BookingDetails
	{
		//	I commented this out because it caused an issue   - Corban-Lee
		//
		//		public virtual ICollection<name> BookingsId { get; set; }

		public int BookingsId { get; set; }

		public int CustomerId { get; set; }

		public int PlayerId { get; set; }

		public int AlleyLaneId { get; set; }

		public int PlayerNo { get; set; }

		public DateTime Date { get; set; }

		public DateTime Time { get; set; }

		public string Status { get; set; }
	}		
}
